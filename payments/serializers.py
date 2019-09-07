import json
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_text
from django.template.loader import render_to_string
from rest_framework.serializers import ModelSerializer
from django.conf import settings

from .models import AddToCart


class PaySerializer(ModelSerializer):
    class Meta:
        model = AddToCart
        fields = ('imp_uid',)

    def as_iamport(self):
        # 본 Form의 Hidden 필드 위젯
        hidden_fields = mark_safe(''.join(smart_text(field) for field in self.hidden_fields()))
        # IMP.request_pay의 인자로 넘길 인자 목록
        fields = {
            'merchant_uid': str(self.instance.merchant_uid),
            'name': self.instance.name,
            'amount': self.instance.amount,
            'email': self.instance.email,
        }
        return hidden_fields + render_to_string('payments/_iamport.html', {
            'json_fields': mark_safe(json.dumps(fields, ensure_ascii=False)),
            'iamport_shop_id': settings.IAMPORT_SHOP_ID, #'iamport' # 개인 상점 아이디로 변경
        })

    def save(self):
        order = super().save(commit=False)
        order.update()
        # order.status = 'paid'  # 아임포트 API를 통한 확인 후에 변경
        # order.save()
        return order