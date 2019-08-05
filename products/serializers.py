from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *


# ProductThumnail Model Serializer
class ThumnailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductThumnail
        fields = '__all__'


# ProductDetailImage Model Serializer
class DetailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetailImage
        fields = '__all__'


# ProductOption Model Serializer
class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'


# Review Model Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# PDQnA Model Serializer
class PDQnASerializer(serializers.ModelSerializer):
    class Meta:
        model = PDQnA
        fields = '__all__'


# Product Model Serializer
class ProductSerializer(serializers.ModelSerializer):
    # 읽기 전용으로, serializer 클래스에서 메서드를 호출하여 값을 가져옴
    thumnail_images = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'brand_name', 'name', 'discount_rate', 'price', 'review_count', 'star_avg', 'thumnail_images']

    # 함수명은 get_[related_name field]로써,
    # def get_[related_name](self, [models.py에서 해당 class 내 related_name의 변수명]): 을 가져오면 됨
    def get_thumnail_images(self, product):
        # filter는 object를 이용해 가져옴으로써, slice(잘라서)를 통해 원하는 내용을 가져올 수 있음
        # Queryset처럼 일반적으로 해당 부분만 불러오도록 뒤에[0] 등을 사용하면 Err 발생함
        thumnail_images = ProductThumnail.objects.filter(product=product)[0:1]
        # 인스턴스에 해당 내용을 넣어 실제 filtering을 실시함
        serializer = ThumnailImageSerializer(instance=thumnail_images, many=True)
        # filtering된 내용의 data를 반환함
        return serializer.data


# Product Model Detail Serializer
class ProductDetailSerializer(serializers.ModelSerializer):
    thumnail_images = ThumnailImageSerializer(source='product_thumnail', many=True)
    detail_images = DetailImageSerializer(source='product_detail_images', many=True)
    product_option = ProductOptionSerializer(source='product_options', many=True)
    review = ReviewSerializer(source='reviews', many=True)
    pdqna = PDQnASerializer(source='question', many=True)

    class Meta:
        model = Product
        fields = '__all__'


# Category Model Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Category Model Detail Serializer
class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='category', many=True)

    class Meta:
        model = Category
        fields = '__all__'


# Review Model Create Serializer
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'star_score', 'image', 'comment']


# Review Model Update Serializer
class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['star_score', 'image', 'comment']


# PDQnA Model Create Serializer
class PDQnACreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDQnA
        fields = ['product', 'type', 'comment']


# OrderItem Model Response Serializer
# Order Create 요청을 했을 때 응답하는 Serializer
class OrderItemResponseSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='product.brand_name')
    product = serializers.CharField(source='product.name')
    product_id = serializers.CharField(source='product.id')
    product_option = serializers.CharField(source='product_option.name')

    class Meta:
        model = OrderItem
        exclude = ['id', 'user', 'order']

    def to_representation(self, instance):
        serializer_data = super().to_representation(instance)
        thumnail_image = Product.objects.get(name=serializer_data['product']).product_thumnail.all()[0].image
        quantity = serializer_data['quantity']
        price = ProductOption.objects.get(name=serializer_data['product_option']).price
        total_price = quantity * price
        serializer_data['thumnail_image'] = thumnail_image
        serializer_data['total_price'] = total_price
        return serializer_data


# OrderItem Model Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    brand_name = serializers.CharField(source='product.brand_name')
    product = serializers.CharField(source='product.name')
    product_id = serializers.CharField(source='product.id')
    deliver_fee = serializers.CharField(source='product.deliver_fee')
    deliver = serializers.CharField(source='product.deliver')
    product_option = serializers.CharField(source='product_option.name')

    class Meta:
        model = OrderItem
        exclude = ['order']

    def to_representation(self, instance):
        serializer_data = super().to_representation(instance)
        thumnail_image = Product.objects.get(name=serializer_data['product']).product_thumnail.all()[0].image
        quantity = serializer_data['quantity']
        price = ProductOption.objects.get(name=serializer_data['product_option']).price
        total_price = quantity * price
        serializer_data['thumnail_image'] = thumnail_image
        serializer_data['total_price'] = total_price
        return serializer_data


# OrderItem Model Create Serializer
class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'product_option', 'quantity']


# OrderItem Model Update Serializer
class OrderItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['quantity']

    def to_representation(self, instance):
        serializer_data = super().to_representation(instance)
        quantity = serializer_data['quantity']
        price = ProductOption.objects.get(name=instance.product_option).price
        total_price = quantity * price
        serializer_data['total_price'] = total_price
        return serializer_data

# Order Model Serializer
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    order_list = OrderItemResponseSerializer(source='orderitems', many=True)

    class Meta:
        model = Order
        fields = '__all__'


# Order Model Create Serializer
# 장바구니 아이템을 구매할 때
class OrderFromCartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['user']


# Order Model Create Serializer
# 바로 구매할 때
class OrderDirectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['user']
