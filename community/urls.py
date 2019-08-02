from django.urls import path
from .api_views import *

urlpatterns = [
    path('photo/', PhotoListAPIView.as_view()),
    path('photo/<int:pk>/', PhotoDetailAPIView.as_view()),

    # 집들이 탭 화면
    path('housewarming/', HousewarmingAPIView.as_view()),
    # 집들이 상품 상세 화면
    path('housewarming/<int:pk>/',HousewarmingDetailAPIView.as_view()),

    # 커뮤니티 홈 화면
    path('home/', CommunityHomeAPIView.as_view()),
]
