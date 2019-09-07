from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import status, Response
from rest_framework.decorators import api_view
from .models import AddToCart
from .serializers import PaySerializer


@api_view(['POST'])
def order_new(request, item_id): # 특정 아이템 하나만 지정
    item = get_object_or_404(Item, pk=item_id) # 아이템 획득
    order = AddToCart.objects.create(user=request.user, item=item, name=item.name, amount=item.amount)
    return redirect('payments:order_pay', item_id, str(order.merchant_uid))

@api_view(['POST', 'GET'])
def order_pay(request, item_id, merchant_uid):
    order = get_object_or_404(AddToCart, user=request.user, merchant_uid=merchant_uid, status='ready')
    if request.method == 'POST':
        serializer = PaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('profile')
    else:
        serializer = PaySerializer(AddToCart.objects.all(), many=True)
        return render(request, 'payments/pay_form.html', {
           'form': form,
        })