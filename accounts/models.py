from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Social Login additional info
    TYPE_DJANGO, TYPE_KAKAO, TYPE_GOOGLE, TYPE_NAVER = 'django', 'kakao', 'google', 'naver'
    CHOICES_TYPE = (
        (TYPE_KAKAO, '카카오'),
        (TYPE_GOOGLE, '구글'),
        (TYPE_NAVER, '네이버'),
    )
    # Social service type
    type = models.CharField('유형', choices=CHOICES_TYPE, max_length=12, default=TYPE_DJANGO)
    # Social service에서 보낸 UniqueID
    unique_user_id = models.CharField(max_length=50, null=True)
    # Social service에서 보낸 profile Image
    social_profile = models.TextField(blank=True)

    # House of today user info
    # 이메일
    email = models.EmailField('이메일', unique=True)
    # 성별(1 = 남자, 2 = 여자)
    gender = models.PositiveIntegerField(blank=True, null=True)
    # 생일
    birthday = models.DateField(blank=True, null=True)
    # 한줄 소개
    message = models.TextField(blank=True)
    # 프로필 이미지
    profile = models.ImageField(upload_to='user_image/profile/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.username + "(" + self.type + ")"

    class Meta:
        ordering = ['id']
