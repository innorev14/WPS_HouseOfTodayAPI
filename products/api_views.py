from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from django.db.models import Q


# 스토어/카테고리 리스트 관련 뷰
class CategoryListView(generics.ListAPIView):
    """
        스토어/카테고리 리스트를 불러옵니다.

        ---
        # 내용
            - id : 카테고리의 고유 ID
            - name : 카테고리 이름
            - image : 카테고리 이미지 URL
    """
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


# 스토어/카테고리 디테일 관련 뷰
class CategoryDetailView(generics.RetrieveAPIView):
    """
        스토어/카테고리 리스트에서 특정 id를 가지는 데이터를 불러옵니다.

        ---
        # 내용
            - id : 카테고리의 고유 ID

            - products : 카테고리에 속한 상품
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - price : 상품 가격
                - review_count : 리뷰 수
                - star_avg : 리뷰 평점
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                    - product : 썸네일 이미지가 속한 상품의 고유 ID
            - name : 카테고리 이름
            - image : 카테고리 이미지 URL
    """
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = (AllowAny,)


# 스토어/상품 리스트 관련 뷰
class ProductListView(generics.ListAPIView):
    """
        상품 리스트를 불러옵니다.

        ---
        # 내용
            - id : 상품의 고유 ID
            - brand_name : 상품의 브랜드 이름
            - name : 상품 이름
            - price : 상품 가격
            - review_count : 리뷰 수
            - star_avg : 리뷰 평점
            - thumnail_images : 상품 썸네일 이미지
                - id : 썸네일 이미지의 고유 ID
                - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID
    """
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


# 스토어/상품 디테일 관련 뷰
class ProductDetailView(generics.RetrieveAPIView):
    """
        상품 리스트에서 특정 id를 가지는 데이터를 불러옵니다.

        ---
        # 내용
            - id : 상품의 고유 ID

            - thumnail_images : 상품 썸네일 이미지
                - id : 썸네일 이미지의 고유 ID
                - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - detail_images : 상품 정보 이미지
                - id : 정보 이미지의 고유 ID
                - image : 정보 이미지 URL
                - product : 정보 이미지가 속한 상품의 고유 ID

            - product_option : 상품 옵션
                - id : 옵션의 고유 ID
                - type : 옵션 타입
                - name : 옵션 이름
                - price : 옵션 가격
                - product : 옵션이 속한 상품의 고유 ID

            - review : 상품 리뷰
                - id : 리뷰의 고유 ID
                - star_score : 리뷰 별점
                - image : 리뷰 이미지
                - comment : 리뷰 내용
                - created : 리뷰 생성 일자
                - user : 리뷰 작성자
                - product : 리뷰가 속한 상품의 고유 ID
                - helpful : 리뷰 '도움이 돼요' - 아직 구현되지 않음

            - pdqna : 상품 QnA
                - id : QnA의 고유 ID
                - type : 질문 타입
                - comment : 질문 내용
                - completed : 답변 체크(미답변 = False, 답변완료 = True)
                - created : 질문 생성 일자
                - a_author : 답변 작성자
                - a_comment : 답변 내용
                - a_created : 답변 생성 일자
                - user : 질문 작성자
                - product : QnA가 속한 상품의 고유 ID

            < 상품 정보 데이터 >
            - name : 상품 이름
            - price : 상품 가격
            - brand_name : 상품 브랜드 이름
            - detail_name : 품명 및 모델명
            - detail_color : 색상
            - detail_size : 크기
            - detail_component : 구성품
            - detail_auth : KC인증 필 유무
            - detail_cost : 배송 설치비용
            - detail_standard : 품질보증기준
            - detail_mfc : 제조자
            - detail_mis : 제조국(수입여부)
            - detail_as : A/S책임자와 전화번호

            < 교환 및 환불 정보 데이터 >
            - return_fee : 반품/배송비
            - exchange_fee : 교환/배송비
            - return_address : 보내실 곳

            < 배송 관련 안내 정보 데이터 >
            - deliver : 배송
            - deliver_fee : 배송비
            - deliver_no_go : 배송불가 지역
            - deliver_fee_diff : 지역별 차등 배송비

            - created : 상품 업로드 생성 일자
            - discount_rate : 할인율
            - star_avg : 리뷰 평점
            - review_count : 리뷰 수
            - category : 상품이 속한 카테고리의 고유 ID

    """
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)


# 스토어/스토어홈 관련 뷰
# google 검색어 : how to DRF serializer combine
# 참조 : https://stackoverflow.com/questions/45414928/combining-two-different-serializers-into-one-view-returning-named-json-arrays
class StoreHomeView(generics.ListAPIView):
    """
        스토어 홈 관련 정보를 모두 불러옵니다.

        ---
        # 내용
            - todaydeal : 오늘의 딜
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - review_count : 리뷰 수
                - star_avg : 리뷰 평점
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - categories: 카테고리
                - id : 카테고리의 고유 ID
                - name : 카테고리 이름
                - image : 카테고리 이미지 URL

            - poular_products : 인기 상품
                - id : 상품의 고유 ID
                    - brand_name : 상품의 브랜드 이름
                    - name : 상품 이름
                    - discount_rate : 할인율
                    - price : 상품 가격
                    - thumnail_images : 상품 썸네일 이미지
                        - id : 썸네일 이미지의 고유 ID
                        - image : 썸네일 이미지 URL
                    - product : 썸네일 이미지가 속한 상품의 고유 ID
    """
    renderer_classes = [JSONRenderer]
    serializer_class_product = ProductSerializer
    serializer_class_category = CategorySerializer

    permission_classes = (AllowAny,)

    def get_queryset_product(self):
        hot_deal_num = HotDealNumber.objects.all()

        result = Product.objects.all().filter(Q(id=hot_deal_num[0].product_rnd_number)
                                              | Q(id=hot_deal_num[1].product_rnd_number)
                                              | Q(id=hot_deal_num[2].product_rnd_number)
                                              | Q(id=hot_deal_num[3].product_rnd_number))
        return result

        # return Product.objects.all()

    def get_queryset_category(self):
        return Category.objects.all()

    def get_queryset_popularproducts(self):
        return Product.objects.all().order_by('-star_avg')

    def list(self, request, *args, **kwargs):
        todaydeal = self.serializer_class_product(self.get_queryset_product(), many=True)
        categories = self.serializer_class_category(self.get_queryset_category(), many=True)
        popular_products = self.serializer_class_product(self.get_queryset_popularproducts(), many=True)

        return Response({
            'todaydeal': todaydeal.data,
            'categories': categories.data,
            'popular_products': popular_products.data
        })


# 스토어/랭킹 관련 뷰
class RankingView(generics.ListAPIView):
    """
        랭킹 관련 정보를 모두 불러옵니다.

        ---
        # 내용
            - best100 : 카테고리별 BEST 100 정보(상품 100개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - review_count : 리뷰 수
                - star_avg : 리뷰 평점
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - light_homedeco : 조명&홈데코 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - daily_supplies : 생활용품 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - fabric : 패브릭 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - kitchenware : 주방용품 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - home_appliances : 가전제품 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - companion_animal : 반려동물 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - furniture : 가구 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID
    """
    renderer_classes = [JSONRenderer]

    serializer_class_product = ProductSerializer
    # 각 Category별 제품을 분리시켜 받아오기 위해 사용.
    serializer_class_category_in_product = ProductSerializer
    # serializer_class_category_in_product = ProductSerializer(source='category', many=True)

    permission_classes = (AllowAny,)

    # 카테고리별 best100
    def get_queryset_product(self):
        return Product.objects.all().order_by('-star_avg')[0:100]

    # 조명&홈데코(category 명칭: 홈데코&조명)
    def get_queryset_category_in_product4(self):
        return Product.objects.filter(category__id='4').order_by('-star_avg')[0:10]

    # 생활용품(category 명칭: 수납/생활)
    def get_queryset_category_in_product6(self):
        return Product.objects.filter(category__id='6').order_by('-star_avg')[0:10]

    # 패브릭
    def get_queryset_category_in_product3(self):
        return Product.objects.filter(category__id='3').order_by('-star_avg')[0:10]

    # 주방용품(category 명칭: 주방)
    def get_queryset_category_in_product7(self):
        return Product.objects.filter(category__id='7').order_by('-star_avg')[0:10]

    # 가전제품
    def get_queryset_category_in_product5(self):
        return Product.objects.filter(category__id='5').order_by('-star_avg')[0:10]

    # 반려동물
    def get_queryset_category_in_product10(self):
        return Product.objects.filter(category__id='10').order_by('-star_avg')[0:10]

    # 가구
    def get_queryset_category_in_product2(self):
        return Product.objects.filter(category__id='2').order_by('-star_avg')[0:10]

    def list(self, request, *args, **kwargs):
        best100 = self.serializer_class_product(self.get_queryset_product(), many=True)
        light_homedeco = self.serializer_class_category_in_product(self.get_queryset_category_in_product4(), many=True)
        daily_supplies = self.serializer_class_category_in_product(self.get_queryset_category_in_product6(), many=True)
        fabric = self.serializer_class_category_in_product(self.get_queryset_category_in_product3(), many=True)
        kitchenware = self.serializer_class_category_in_product(self.get_queryset_category_in_product7(), many=True)
        home_appliances = self.serializer_class_category_in_product(self.get_queryset_category_in_product5(), many=True)
        companion_animal = self.serializer_class_category_in_product(self.get_queryset_category_in_product10(),
                                                                     many=True)
        furniture = self.serializer_class_category_in_product(self.get_queryset_category_in_product2(), many=True)

        return Response({
            'best100': best100.data,
            'light_homedeco': light_homedeco.data,
            'daily_supplies': daily_supplies.data,
            'fabric': fabric.data,
            'kitchenware': kitchenware.data,
            'home_appliances': home_appliances.data,
            'companion_animal': companion_animal.data,
            'furniture': furniture.data,
        })
        # 카테고리별 best100 : 'best100'
        # 조명&홈데코 4 : 'light_homedeco'
        # 생활용품 6 : 'daily_supplies'
        # 패브릭 3 : 'fabric'
        # 주방용품 7 : 'kitchenware'

        # 가전제품 5 : 'home_appliances'
        # 반려 동물 10 : 'companion_animal'
        # 가구 2 : 'furniture'

        # products = ProductSerializer(source='category', many=True)


# 스토어/상품 리뷰 생성 관련 뷰
class ReviewCreateAPIView(generics.CreateAPIView):
    """
        상품 리뷰를 생성합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있으며, 생성된 값이 리턴됩니다.
        image의 경우, 파일을 업로드해야 하기 때문에 json으로 요청하실 수 없고 Postman을 사용해야 합니다.

        # 내용
            - product : "리뷰가 속한 상품의 고유 ID"
            - star_score : "상품에 대한 리뷰 점수"
            - image : "업로드 할 리뷰 이미지"
            - comment : "업로드 할 내용"
    """
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 스토어/상품 리뷰 수정 관련 뷰
class ReviewUpdateAPIView(generics.UpdateAPIView):
    """
        상품 리뷰의 특정 id를 가지는 데이터를 수정합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있으며, 수정된 값이 리턴됩니다.
        요청은 PUT, FETCH로 나뉩니다.
        image의 경우, 파일을 업로드해야 하기 때문에 json으로 요청하실 수 없고 Postman을 사용해야 합니다.

        # 내용
            - star_score : "상품에 대한 리뷰 점수"
            - image : "업로드 할 리뷰 이미지"
            - comment : "업로드 할 내용"
    """
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer


# 스토어/상품 문의 생성 관련 뷰
class PDQnACreateAPIView(generics.CreateAPIView):
    """
        상품 문의를 생성합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있으며, 수정된 값이 리턴됩니다.

        # 내용
            - product : "문의가 속한 상품의 고유 ID"
            - type : "상품에 대한 문의유형"
            - comment : "문의 할 내용"
    """
    queryset = PDQnA.objects.all()
    serializer_class = PDQnACreateSerializer

    # ############ def perform_create(self, serializer): 사용시 주의사항 ############
    # serializer.save는 단 한번만 이뤄져야 함. 여러번 save를 하여 각 필드마다 넣을 수 있으나,
    # 그럴 경우 receiver에서 여러번 실행될 수 있기 때문에 save할때 한번에 여러 필드를 저장하는게 맞다.
    # 왠만한 stackoverflow 답변 글에서도 serializer.save() 는 한번만 사용하도록 답변이 달림.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 스토어/상품 리뷰 삭제 관련 뷰
class PDQnADeleteAPIView(generics.DestroyAPIView):
    """
        상품 문의의 특정 id를 가지는 데이터를 삭제합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        상품 문의의 고유 ID를 입력하면 삭제됩니다.
    """
    queryset = PDQnA.objects.all()


# 장바구니 리스트 관련 뷰
class OrderItemListAPIView(generics.ListAPIView):
    """
        해당 유저의 장바구니에 담긴 아이템 리스트를 불러옵니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        # 내용
            - id : 장바구니 아이템의 고유 ID
            - user : 해당 유저 이름
            - brand_name : 해당 아이템의 상품 브랜드
            - product : 해당 아이템의 상품 이름
            - deliver_fee : 배송비에 관한 내용
            - deliver : 배송에 관한 내용
            - product_option : 해당 아이템 상품의 옵션
            - quantity : 수량
            - thumnail_image : 해당 아이템 상품의 이미지 URL
            - total_price : 상품의 가격 x 수량
    """
    renderer_classes = [JSONRenderer]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user.id)
        return queryset


# 장바구니 아이템 생성 관련 뷰
class OrderItemCreateAPIView(APIView):
    """
        장바구니 아이템을 생성합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있습니다.

        # 내용
            - product : "장비구니에 담을 상품의 고유 ID"
            - product_option : "장바구니에 담을 상품의 옵션 고유 ID"
            - quantity : "해당 상품 옵션의 수량"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - id : 장바구니 아이템의 고유 ID
            - user : 해당 유저 이름
            - brand_name : 해당 아이템의 상품 브랜드
            - product : 해당 아이템의 상품 이름
            - deliver_fee : 배송비에 관한 내용
            - deliver : 배송에 관한 내용
            - product_option : 해당 아이템 상품의 옵션
            - quantity : 수량
            - thumnail_image : 해당 아이템 상품의 이미지 URL
            - total_price : 상품의 가격 x 수량
    """

    def post(self, request, *args, **kwargs):
        # pass
        # pass로 입력하고 브레이킹 포인트를 걸면 request에 넘어오는 데이터를
        # 볼 수 있다.

        # 새 post를 작성
        # author는 request.user를 사용

        # request.data에 데이터가 전달됨
        # 전달받은 데이터를 data 키워드 인수로 PostSerializer 생성에 전달, serializer 생성
        # serializer.is vaild() 호출로 validation 점검
        # vaild 하다면 serializer.save()를 호출해서 ModelSerializer로 DB row 생성
        # -> 이 과정에서, save()에 user를 request.user로 전달
        #    완료했다면, Response에 serializer의 data를 전달해서 리턴
        # valid하지 않다면 Response에 serializers.errors를 전달

        # post serializer instance 생성
        serializer = OrderItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            # vaild 하다면 serializer.save()를 호출해서 ModelSerializer로 DB row 생성
            instance = serializer.save(user=request.user)
            # 돌아오는 데이터에는 입력한 데이터가 돌아와야 한다.
            return Response(OrderItemSerializer(instance).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 장바구니 아이템 수량 수정 및 삭제 관련 뷰
class OrderItemChangeAPIView(APIView):
    """
        장바구니 아이템 리스트에서 특정 id를 가지는 데이터의 수량을 변경하거나 데이터를 삭제합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있습니다.
        DELETE 요청의 경우, 리턴되는 내용이 없습니다.

        # 내용
            - quantity : "해당 아이템 상품의 수량"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - quantity : 변경된 해당 아이템 상품의 수량
            - total_price : 상품의 가격 x 수량
    """

    def get_object(self, pk):
        try:
            return OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = OrderItemUpdateSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 주문 내역 리스트 관련 뷰
class OrderListAPIView(generics.ListAPIView):
    """
        해당 유저의 주문 내역 리스트를 불러옵니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        # 내용
            - id : 주문 내역의 고유 ID
            - user : 해당 유저 이름
            - order_list : 주문한 상품의 리스트
                - brand_name : 주문한 상품의 브랜드
                - product : 주문한 상품의 이름
                - product_option : 주문한 상품의 옵션
                - quantity : 수량
                - thumnail_image : 주문한 상품의 이미지 URL
                - total_price : 상품의 가격 x 수량
    """
    renderer_classes = [JSONRenderer]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user.id)
        return queryset


# 장바구니 구매하기 생성 관련 뷰
class OrderFromCartCreateAPIView(APIView):
    """
        장바구니에 담긴 아이템을 구매 요청합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있습니다.
        장바구니에 담긴 아이템의 고유 ID를 이용해서 선택해서 보낼 수 있습니다.
        큰따옴표(")를 사용해서 보내주세요.
        'pk_list'는 장바구니 아이템의 고유 ID를 나타내며, '(콤마)'로 구분해서 보내면 됩니다.
        *****콤마 사이에 띄어쓰기 하지 말아주세요!
        *****한 가지만 보낼 때는 콤마를 붙이지 말아주세요!

        # 내용
            - pk_list : "장바구니에 담긴 아이템의 고유 ID"

            ex) 장바구니 리스트에 id가 1,2,3이 들어있을 때 1번만 선택할 경우

                - pk_list : "1"

            ex) 장바구니 리스트에 id가 1,2,3이 들어있을 때 2,3번만 선택할 경우

                - pk_list : "2,3"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - id : 주문 내역의 고유 ID
            - user : 해당 유저 이름
            - order_list : 주문한 상품의 리스트
                - brand_name : 주문한 상품의 브랜드
                - product : 주문한 상품의 이름
                - product_option : 주문한 상품의 옵션
                - quantity : 수량
                - thumnail_image : 주문한 상품의 이미지 URL
                - total_price : 상품의 가격 x 수량
    """

    def post(self, request, *args, **kwargs):
        serializer = OrderFromCartCreateSerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save(user=request.user)
            # pk_list를 받아서 split을 통해 숫자 리스트를 받음
            pk_list = request.data['pk_list'].replace('"', '').split(',')

            for pk in pk_list:
                # orderitem에서 해당 pk 값을 가진 orderitem을 얻음
                orderitem = OrderItem.objects.get(pk=int(pk))
                # instance.id를 통해 order의 id를 얻고, orderitem의 order에 넣음(order와 연결)
                orderitem.order_id = instance.id
                # None을 통해 user와의 관계를 끊음
                orderitem.user = None
                orderitem.save()

            return Response(OrderSerializer(instance).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  바로 구매하기 생성 관련 뷰
class OrderDirectCreateAPIView(APIView):
    """
        해당 상품을 바로 구매하는 요청을 합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.


        다음과 같은 내용으로 요청할 수 있습니다.
        직접 구매하는 경우, 장바구니를 통해서 구매하는 것이 아니기 때문에
        구매하는 상품, 상품 옵션, 수량에 대한 정보가 필요합니다.

        'pd_id'는 직접 구매하는 상품의 고유 ID입니다.
        'po_list'는 직접 구매하는 상품 옵션의 고유 ID입니다.
        'qty_list'는 직접 구매하는 상품 옵션의 수량입니다.

        다음 항목을 큰따옴표(")를 사용해서 보내주세요.
        'pd_id'의 경우 직접 구매이기 때문에 상품은 하나이므로 값을 하나만 보내주세요.
        'po_list'의 경우 옵션을 여러가지 선택할 수 있기 때문에 ',(콤마)'로 구분해서 보내면 됩니다.
        'qty_list'의 경우 선택한 옵션의 순서대로 ',(콤마)'로 구분해서 보내면 됩니다.
        *****콤마 사이에 띄어쓰기 하지 말아주세요!
        *****한 가지만 보낼 때는 콤마를 붙이지 말아주세요!

        # 내용
            - pd_id : "직접 구매하는 상품의 고유 ID"
            - po_list : "직접 구매하는 상품 옵션의 고유 ID"
            - qty_list : "직접 구매하는 상품 옵션의 수량"

            ex) 상품 id가 1번이고
                상품 옵션 id가 1번에 수량은 3개를 선택했을 경우

                - pd_id : "1"
                - po_list : "1"
                - qty_list : "3"

            ex) 상품 id가 1번이고
                상품 옵션 id가 1번에 수량은 2개,
                상품 옵션 id가 2번에 수량은 5개,
                상품 옵션 id가 3번에 수령은 7개를 선택했을 경우

                - pd_id : "1"
                - po_list : "1,2,3"
                - qty_list : "2,5,7"


        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - id : 주문 내역의 고유 ID
            - user : 해당 유저 이름
            - order_list : 주문한 상품의 리스트
                - brand_name : 주문한 상품의 브랜드
                - product : 주문한 상품의 이름
                - product_option : 주문한 상품의 옵션
                - quantity : 수량
                - thumnail_image : 주문한 상품의 이미지 URL
                - total_price : 상품의 가격 x 수량
    """

    def post(self, request, *args, **kwargs):
        serializer = OrderDirectCreateSerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save(user=request.user)
            # pd_id : 상품의 고유 id
            pd_id = request.data['pd_id'].replace('"', '')
            # po_list : 상품 옵션의 고유 id를 split을 통해 숫자 리스트로 받음
            po_list = request.data['po_list'].replace('"', '').split(',')
            # qty_list : 상품 옵션 수량을 split을 통해 숫자 리스트로 받음
            qty_list = request.data['qty_list'].replace('"', '').split(',')

            for idx in range(len(po_list)):
                # 장바구니에 들어가는 것이 아니기 때문에 orderitem을 직접 생성
                orderitem = OrderItem()
                # 상품 id를 넣음
                orderitem.product_id = int(pd_id)
                # 상품 옵션 id를 넣음
                orderitem.product_option_id = int(po_list[idx])
                # instance에서 order의 id를 얻어서 넣음(order와 연결)
                orderitem.order_id = instance.id
                # 상품 수량을 넣음
                orderitem.quantity = int(qty_list[idx])
                # None을 통해 user와의 관계를 끊음
                orderitem.user = None
                orderitem.save()

            return Response(OrderSerializer(instance).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
