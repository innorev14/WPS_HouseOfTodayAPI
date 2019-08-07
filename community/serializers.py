from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *

# 사진 탭 댓글 관련 serializer
class PhotoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = '__all__'


class PhotoCommentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = ['author_profile_image', 'author', 'text']


class PhotoSerializer(serializers.ModelSerializer):
    comments = SerializerMethodField()

    class Meta:
        model = Photo
        fields = ['id', 'author', 'author_profile_image', 'author_profile_comment', 'image', 'product_image', 'product_id', 'hit_count', 'like_count',
                  'scrap_count', 'comment_count', 'text', 'comments']

    def get_comments(self, photo):
        first_comment = PhotoComment.objects.filter(photo=photo)[0:1]
        serializer = PhotoCommentSimpleSerializer(instance=first_comment, many=True)
        return serializer.data

class PhotoDetailSerializer(serializers.ModelSerializer):
    photo_comments = PhotoCommentSerializer(source='comments', many=True)

    class Meta:
        model = Photo
        fields = '__all__'


# 커뮤니티-홈의 오늘의 사진 부분에 대한 Serializer임.
class TodayPictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ['id', 'author', 'image', 'author_profile_image']


# 집들이 탭 메인 serializer
class HousewarmingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housewarming
        fields = ['id','cover_image','title','author_profile','author','scrap_count','hit_count']


# 집들이 탭 게시글 내 여러 사진&글 serializer
class HousewarmingDetailContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailContent
        fields = ['id','title','image','text']


# 집들이 탭 게시글 내 여러 댓글 serializer
class HousewarmingCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousewarmingComment
        fields = ['id','author','author_profile_image','text','created']


# 집들이 탭 각각의 게시글 정보 serializer (HousewarmingDetailContentSerializer + HousewarmingCommentSerializer)
class HousewarmingDetailSerializer(serializers.ModelSerializer):
    housewarming_detail_content = HousewarmingDetailContentSerializer(source='detail_contents', many=True)
    housewarming_comments = HousewarmingCommentSerializer(source='comments', many=True)

    class Meta:
        model = Housewarming
        fields = '__all__'



