from django.contrib import admin
from .models import *


# Category 관련 Admin
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
    list_display = ['id', 'name', 'image']


# Product 관련 Admin
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'brand_name', 'category', 'detail_name', 'detail_color', 'detail_size',
              'detail_component', 'detail_auth', 'detail_cost', 'detail_standard', 'detail_mfc', 'detail_mis',
              'detail_as', 'return_fee', 'exchange_fee', 'return_address', 'deliver', 'deliver_fee', 'deliver_no_go',
              'deliver_fee_diff', 'discount_rate', 'star_avg', 'review_count']
    list_display = ['id', 'name', 'price', 'brand_name', 'star_avg', 'review_count']


# Product Thumnail 관련 Admin
class ProductThumnailAdmin(admin.ModelAdmin):
    fields = ['image', 'product']
    list_display = ['id', 'image', 'product']


# Product Detail 관련 Admin
class ProductDetailImageAdmin(admin.ModelAdmin):
    fields = ['image', 'product']
    list_display = ['id', 'image', 'product']


# Product Option 관련 Admin
class ProductOptionAdmin(admin.ModelAdmin):
    fields = ['type', 'name', 'price', 'product']
    list_display = ['id', 'type', 'name', 'price', 'product']


# Product Review 관련 Admin
class ReviewAdmin(admin.ModelAdmin):
    fields = ['user', 'product', 'star_score', 'image', 'comment']
    list_display = ['id', 'user', 'product', 'star_score', 'image', 'comment', 'created']


# Product QnA Admin
class PDQnAAdmin(admin.ModelAdmin):
    fields = ['type', 'comment', 'completed', 'user', 'product', 'a_author', 'a_comment']
    list_display = ['id', 'type', 'comment', 'completed', 'created', 'user', 'product', 'a_author', 'a_comment',
                    'a_created']


# 오늘의 딜 숫자 모델 Admin
class HotDealNumberAdmin(admin.ModelAdmin):
    fields = ['product_rnd_number']
    list_display = ['id', 'product_rnd_number', 'updated']


# 장바구니 아이템 Admin
class OrderItemAdmin(admin.ModelAdmin):
    fields = ['user', 'order', 'product', 'product_option', 'quantity']
    list_display = ['id', 'user', 'order', 'product', 'product_option', 'quantity']


# 주문 내역 Admin
class OrderAdmin(admin.ModelAdmin):
    fields = ['user']
    list_display = ['id', 'user']


# CronTab 로그 기록 Admin
class CronLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'cronjob_comment', 'cron_date']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductThumnail, ProductThumnailAdmin)
admin.site.register(ProductDetailImage, ProductDetailImageAdmin)
admin.site.register(ProductOption, ProductOptionAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(PDQnA, PDQnAAdmin)
admin.site.register(HotDealNumber, HotDealNumberAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CronLog, CronLogAdmin)
