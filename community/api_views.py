from django.db.models import Q

from .models import *
from .serializers import *

from products.models import *
from products.serializers import *

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny


class PhotoListAPIView(generics.ListAPIView):
    """
        커뮤니티/사진 리스트를 불러옵니다.

        ---
        # 내용
            - id : 사진 고유의 ID
            - author : 작성자
            - image : 사진 이미지 URL
            - hit_count : 조회 수
            - like_count : '좋아요' 수
            - scrap_count : 스크랩 수
            - comment_count : 댓글 수
            - text : 사진 내용
            - comments : 사진에 포함된 첫번째 댓글
                - author_profile_image : 댓글 작성자의 프로필 이미지 URL
                - author : 댓글 작성자
                - text : 댓글 내용
    """
    renderer_classes = [JSONRenderer]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (AllowAny,)


class PhotoDetailAPIView(generics.RetrieveAPIView):
    """
        커뮤니티/사진 리스트에서 특정 id를 가지는 데이터를 불러옵니다.

        ---
        # 내용
            - id : 사진 고유의 ID
            - photo_comments : 사진에 포함된 전체 댓글
                - id : 댓글의 고유 ID
                - author : 댓글 작성자
                - author_profile_image : 댓글 작성자의 프로필 이미지 URL
                - text : 댓글 내용
                - created : 댓글 생성 일자
                - photo : 댓글이 속한 사진의 고유 ID
            - category : 작성자가 지정한 카테고리 ex) 10평대 | 모던 스타일
            - created : 사진 글 생성 일자
            - image : 사진 이미지 URL
            - axis_left : 사진 이미지 속 left 좌표(%)
            - axis_top : 사진 이미지 속 top 좌표(%)
            - product_image : 사진 이미지와 관련된 상품 이미지 URL
            - product_id : 관련된 상품의 고유 ID
            - text : 사진 내용
            - author : 작성자
            - author_profile_image : 작성자의 프로필 이미지 URL
            - author_profile_comment : 작성자의 프로필 소개 내용
            - like_count : '좋아요' 수
            - scrap_count : 스크랩 수
            - hit_count : 조회 수
            - comment_count : 댓글 수
    """
    renderer_classes = [JSONRenderer]
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    permission_classes = (AllowAny,)


class HousewarmingAPIView(generics.ListAPIView):
    """
        커뮤니티/집들이 글 전체 개수, 리스트를 불러옵니다.

        ---
        # 내용
            - total_post_count : 집들이 글 전체 개수
            - housewarming_posts : 커뮤니티/집들이 리스트
                - id : 집들이 고유의 ID
                - cover_image : 집들이 글 대표 이미지
                - title : 집들이 글 제목
                - author_profile : 작성자 프로필 이미지
                - author : 작성자
                - scrap_count : 스크랩 수
                - hit_count : 조회 수
    """

    renderer_classes = [JSONRenderer]
    queryset = Housewarming.objects.all()
    serializer_class = HousewarmingSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        return Response({
            'total_post_count': self.queryset.count(),
            'housewarming_posts': self.serializer_class(self.get_queryset(), many=True).data,
        })


class HousewarmingDetailAPIView(generics.RetrieveAPIView):
    """
        커뮤니티/집들이 리스트에서 특정 id를 가지는 데이터를 불러옵니다.
        ---
        # 내용
            - id : 해당 게시글 고유의 ID
            - housewarming_detail_content : 해당 게시글에 속하는 사진&글 목록을 불러옵니다.
                - id : 사진&글 목록 고유 ID
                - title : 사진&글 목록 제목
                - image : 사진&글 목록 사진
                - text : 사진&글 목록 글
            - housewarming_comments : 해당 게시글에 속하는 댓글 목록을 불러옵니다.
                - id : 댓글 고유 ID
                - author : 댓글 작성자
                - author_profile_image : 댓글 작성자 프로필 사진
                - text : 댓글 내용
                - created : 댓글 생성 시간
            - title : (해당 게시글) 제목
            - created : 생성일자
            - author : 작성자
            - author_profile : 작성자 프로필 사진
            - like_count : 좋아요 수
            - scrap_count : 스크랩 수
            - hit_count : 조회 수
            - cover_image : 대표 이미지
            - structure : 종류 - 건물
            - floor_space : 종류 - 평수
            - style : 종류 - 스타일
            - work : 종류 - 작업
            - area : 종류 - 분야
            - period : 종류 - 기간
            - family : 종류 - 가족형태
            - detail_part : 종류 - 세부공정
            - location : 종류 - 지역
            - comment_count : 댓글 수
    """
    renderer_classes = [JSONRenderer]
    queryset = Housewarming.objects.all()
    serializer_class = HousewarmingDetailSerializer
    permission_classes = (AllowAny,)


class CommunityHomeAPIView(generics.ListAPIView):
    """
        커뮤니티 홈 관련 정보를 모두 불러옵니다.

        ---
        # 내용
        - today_entry : 캐러셸 대표 게시글 내용 (랜덤으로 나오는 1개의 내용입니다.)
            - id : 해당 게시글 고유의 ID
            - cover_image : 대표 이미지
            - title : (해당 게시글) 제목
            - author_profile : 작성자 프로필 사진
            - author : 작성자
            - scrap_count : 스크랩 수
            - hit_count : 조회 수

        - today_story : 오늘의 스토리 (3개)
            - id : 해당 게시글 고유의 ID
            - cover_image : 대표 이미지
            - title : (해당 게시글) 제목
            - author_profile : 작성자 프로필 사진
            - author : 작성자
            - scrap_count : 스크랩 수
            - hit_count : 조회 수

        - todaydeal : 오늘의 딜(4개)
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

        - today_picture : 커뮤니티/사진 리스트 목록을 불러옵니다(좋아요 순, 8개).
            - id : 사진 고유의 ID
            - author : 작성자
            - image : 사진 이미지 URL
            - hit_count : 조회 수
            - like_count : '좋아요' 수
            - scrap_count : 스크랩 수
            - comment_count : 댓글 수
            - text : 사진 내용
            - comments : 사진에 포함된 첫번째 댓글
                - author_profile_image : 댓글 작성자의 프로필 이미지 URL
                - author : 댓글 작성자
                - text : 댓글 내용

        - best100_category_list : 각 카테고리별 인기상품 목록을 불러옵니다(각 카테고리별 3개).
            - total : 전체 카테고리 중 BEST 정보
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

            - light_homedeco : 조명&홈데코 BEST 정보
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - daily_supplies : 생활용품 BEST 정보
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - fabric : 패브릭 BEST 정보
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - kitchenware : 주방용품 BEST 정보
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

            - companion_animal : 반려동물 BEST 정보
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지 URL
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - furniture : 가구 BEST 정보
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
    # queryset = Housewarming.objects.all()
    serializer_class_story = HousewarmingSerializer
    serializer_class_product = ProductSerializer
    serializer_class_picture = PhotoSerializer
    permission_classes = (AllowAny,)

    # 캐러셸 대표 이미지 및 내용
    def get_queryset_entry(self):
        hot_story_num = HotStoryNumber.objects.all()
        result = Housewarming.objects.all().filter(Q(id=hot_story_num[0].product_rnd_number))
        return result

    # 오늘의 딜(4개)
    def get_queryset_product(self):
        hot_deal_num = HotDealNumber.objects.all()

        result = Product.objects.all().filter(Q(id=hot_deal_num[0].product_rnd_number)
                                              | Q(id=hot_deal_num[1].product_rnd_number)
                                              | Q(id=hot_deal_num[2].product_rnd_number)
                                              | Q(id=hot_deal_num[3].product_rnd_number))
        return result

    # 오늘의 스토리(3개)
    def get_queryset_story(self):
        hot_story_num = HotStoryNumber.objects.all()
        result = Housewarming.objects.all().filter(Q(id=hot_story_num[1].product_rnd_number)
                                              | Q(id=hot_story_num[2].product_rnd_number)
                                              | Q(id=hot_story_num[3].product_rnd_number))
        return result

    # 오늘의 인기 사진 - 좋아요 순으로 정렬 실시(8개).
    def get_queryset_picture(self):
        result = Photo.objects.all().order_by('like_count')[0:8]
        return result

    # 베스트100(3개) - 일단 전체용으로..
    def get_queryset_best100(self):
        return Product.objects.all().order_by('-star_avg')[0:3]

    # ################ 베스트100 내 각 카테고리별 순위 3개씩 나오게 함. #######################
    # 조명&홈데코(category 명칭: 홈데코&조명)
    def get_queryset_category_in_product4(self):
        return Product.objects.filter(category__id='4').order_by('-star_avg')[0:3]

    # 생활용품(category 명칭: 수납/생활)
    def get_queryset_category_in_product6(self):
        return Product.objects.filter(category__id='6').order_by('-star_avg')[0:3]

    # 패브릭
    def get_queryset_category_in_product3(self):
        return Product.objects.filter(category__id='3').order_by('-star_avg')[0:3]

    # 주방용품(category 명칭: 주방)
    def get_queryset_category_in_product7(self):
        return Product.objects.filter(category__id='7').order_by('-star_avg')[0:3]

    # 가전제품
    def get_queryset_category_in_product5(self):
        return Product.objects.filter(category__id='5').order_by('-star_avg')[0:3]

    # 반려동물
    def get_queryset_category_in_product10(self):
        return Product.objects.filter(category__id='10').order_by('-star_avg')[0:3]

    # 가구
    def get_queryset_category_in_product2(self):
        return Product.objects.filter(category__id='2').order_by('-star_avg')[0:3]



    def list(self, request, *args, **kwargs):
        today_entry = self.serializer_class_story(self.get_queryset_entry(), many=True)
        todaydeal = self.serializer_class_product(self.get_queryset_product(), many=True)
        today_story = self.serializer_class_story(self.get_queryset_story(), many=True)
        today_picture = self.serializer_class_picture(self.get_queryset_picture(), many=True)

        best100 = self.serializer_class_product(self.get_queryset_best100(), many=True)
        light_homedeco = self.serializer_class_product(self.get_queryset_category_in_product4(), many=True)
        daily_supplies = self.serializer_class_product(self.get_queryset_category_in_product6(), many=True)
        fabric = self.serializer_class_product(self.get_queryset_category_in_product3(), many=True)
        kitchenware = self.serializer_class_product(self.get_queryset_category_in_product7(), many=True)
        home_appliances = self.serializer_class_product(self.get_queryset_category_in_product5(), many=True)
        companion_animal = self.serializer_class_product(self.get_queryset_category_in_product10(), many=True)
        furniture = self.serializer_class_product(self.get_queryset_category_in_product2(), many=True)

        return Response({
            'today_entry': today_entry.data,
            'today_story': today_story.data,
            'todaydeal': todaydeal.data,
            'today_picture': today_picture.data,
            'best100_category_list': Response({
                'total': best100.data,
                'light_homedeco': light_homedeco.data,
                'daily_supplies': daily_supplies.data,
                'fabric': fabric.data,
                'kitchenware': kitchenware.data,
                'home_appliances': home_appliances.data,
                'companion_animal': companion_animal.data,
                'furniture': furniture.data,
            }).data,
        })

