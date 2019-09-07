from uuid import uuid4
from django.conf import settings
from django.db import models
from django.http import Http404
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.safestring import mark_safe
from accounts.models import User
from products.models import Product, ProductOption

from datetime import datetime
from iamport import Iamport
from jsonfield import JSONField
import pytz

def named_property(name):
    def wrap(fn):
        fn.short_description = name
        return property(fn)
    return wrap

def timestamp_to_datetime(timestamp):
    if timestamp:
        tz = pytz.timezone(settings.TIME_ZONE)
        return datetime.utcfromtimestamp((timestamp)).replace(tzinfo=tz)
    return None

class AddToCart(models.Model):
    # 아이템을 선택한 유저
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addtocart", null=True)
    # # 결제 완료 시, AddToDirect model과의 연결을 위함
    # payment = models.ForeignKey('AddToDirect', on_delete=models.CASCADE, related_name='addtocart', null=True)
    # 선택한 상품
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="addtocart")
    # 선택한 상품 옵션
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE, related_name="addtocart")
    # 선택한 상품 옵션 수량
    quantity = models.PositiveIntegerField(default=1)
    # 결제에 대한 쇼핑몰측의 유니크한 ID, 누가 수정할 수 없도록 editable=False
    merchant_uid = models.UUIDField(default=uuid4, editable=False)
    # 결제상태가paid되면 iamport측에서 전달해주는 id, 처음값은 없을 수 있기에 blank=True
    imp_uid = models.CharField(max_length=100, blank=True)
    # iamport 결제시 상품명
    name = models.CharField(max_length=100, verbose_name='상품명')
    # iamport 결제시 금액
    amount = models.PositiveIntegerField(verbose_name='결제금액')
    photo = models.ImageField()
    # 결제상태
    status = models.CharField(
        max_length=9,
        choices=(
            ('ready', '미결제'),
            ('paid', '결제완료'),
            ('cancelled', '결제취소'),
            ('failed', '결제실패'),
        ),
        default='ready',
        db_index=True)
    meta = JSONField(blank=True, default={})
    # 결제일시
    created_at = models.DateTimeField(auto_now_add=True)
    # 결제상태 변경일시
    updated_at = models.DateTimeField(auto_now=True)

    # 결제준비
    is_ready = property(lambda self: self.status == 'ready')
    # 결제완료
    is_paid = property(lambda self: self.status == 'paid')
    # iamport 측 결제 최종확인
    is_paid_ok = property(lambda self: self.status == 'paid' and self.amount == self.meta.get('amount'))
    # 결제취소
    is_cancelled = property(lambda self: self.status == 'cancelled')
    # 결제실패
    is_failed = property(lambda self: self.status == 'failed')

    receipt_url = named_property('영수증')(lambda self: self.meta.get('receipt_url'))
    cancel_reason = named_property('취소이유')(lambda self: self.meta.get('cancel_reason'))
    fail_reason = named_property('실패이유')(lambda self: self.meta.get('fail_reason', ''))
    paid_at = named_property('결제일시')(lambda self: timestamp_to_datetime(self.meta.get('paid_at')))
    failed_at = named_property('실패일시')(lambda self: timestamp_to_datetime(self.meta.get('failed_at')))
    cancelled_at = named_property('취소일시')(lambda self: timestamp_to_datetime(self.meta.get('cancelled_at')))

    class Meta:
        ordering = ['-id', ]

    # iamport 인증정보
    @property
    def api(self):
        'Iamport Client 인스턴스'
        return Iamport(settings.IAMPORT_API_KEY, settings.IAMPORT_API_SECRET)


    @named_property('결제금액')
    def amount_html(self):
        return mark_safe('<div style="float: right;">{0}</div>'.format(intcomma(self.amount)))

    @named_property('처리결과')
    def status_html(self):
        cls, text_color = '', ''
        help_text = ''
        if self.is_ready:
            cls, text_color = 'fa fa-shopping-cart', '#ccc'
        elif self.is_paid_ok:
            cls, text_color = 'fa fa-check-circle', 'green'
        elif self.is_cancelled:
            cls, text_color = 'fa fa-times', 'gray'
            help_text = self.cancel_reason
        elif self.is_failed:
            cls, text_color = 'fa fa-ban', 'red'
            help_text = self.fail_reason
        html = '''
            <span style="color: {text_color};" title="this is title">
                <i class="{class_names}"></i>
                {label}
            </span>'''.format(class_names=cls, text_color=text_color,label=self.get_status_display())
        if help_text:
            html += '<br/>' + help_text
        return mark_safe(html)

    @named_property('영수증 링크')
    def receipt_link(self):
        if self.is_paid_ok and self.receipt_url:
            return mark_safe('<a href="{0}" target="_blank">영수증</a>'.format(self.receipt_url))

    # 결재내역 갱신'
    def update(self, commit=True, meta=None):
        if self.imp_uid:
            try:
                self.meta = meta or self.api.find(imp_uid=self.imp_uid)
            except Iamport.HttpError:
                raise Http404('Not found {}'.format(self.imp_uid))

            # merchant_uid는 반드시 매칭되어야 함
            assert str(self.merchant_uid) == self.meta['merchant_uid']
            self.status = self.meta['status']
        if commit:
            self.save()

    # 결제내역 취소
    def cancel(self, reason=None, commit=True):
        try:
            meta = self.api.cancel(reason, imp_uid=self.imp_uid) #취소사유 iamport 지원
            assert str(self.merchant_uid) == self.meta['merchant_uid']
            self.update(commit=commit, meta=meta)
        except Iamport.ResponseError as e:  # 취소시 오류 예외처리(이미 취소된 결제는 에러가 발생함)
            self.update(commit=commit)
        if commit:
            self.save()