from django.urls import path
from .api_views import *

app_name = 'payments'

urlpatterns = [
    path('', views.index, name='index'),
    path('<item_id>/order/new/', views.order_new, name='order_new'),
    path('<item_id>/order/<merchant_uid>/pay/', views.order_pay, name='order_pay'),
]