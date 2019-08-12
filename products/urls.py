from django.urls import path
from .api_views import *

urlpatterns = [
    # 전체 카테고리 리스트 경로
    path('category/list/', CategoryListView.as_view()),
    # 특정 pk 값 카테고리 경로
    path('category/<int:pk>/', CategoryDetailView.as_view()),

    # 전체 상품 리스트 경로
    path('product/list/', ProductListView.as_view()),
    # 특정 pk 값 상품 경로
    path('product/<int:pk>/', ProductDetailView.as_view()),
    # 특정 브랜드 이름 상품 경로
    path('product/brand/', ProductBrandView.as_view()),

    # 스토어/스토어홈 경로
    path('storehome/', StoreHomeView.as_view()),
    # 스토어/랭킹 경로
    path('ranking/', RankingView.as_view()),

    # 상품 리뷰 생성 경로
    path('product/review/', ReviewCreateAPIView.as_view()),
    # 상품 리뷰 수정 경로
    path('product/review/<int:pk>/', ReviewUpdateAPIView.as_view()),
    # 상품 리뷰 '도움이 돼요' 경로
    path('product/helpful/', ReviewHelpfulAPIView.as_view()),

    # 상품 Q&A 생성 경로
    path('product/qna/', PDQnACreateAPIView.as_view()),
    # 상품 Q&A 삭제 경로
    path('product/qna/delete/<int:pk>/', PDQnADeleteAPIView.as_view()),

    # 장바구니 아이템 생성 경로
    path('orderitem/', OrderItemCreateAPIView.as_view()),
    # 장바구니 아이템 수정 및 삭제 경로
    path('orderitem/<int:pk>', OrderItemChangeAPIView.as_view()),
    # 장바구니 리스트 경로
    path('cart/', OrderItemListAPIView.as_view()),

    # 장바구니 결제 경로
    path('order_cart/create/', OrderFromCartCreateAPIView.as_view()),
    # 바로 결제 경로
    path('order_direct/create/', OrderDirectCreateAPIView.as_view()),
    # 결제 리스트 경로
    path('order/', OrderListAPIView.as_view()),
]
