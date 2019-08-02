from django.db import models

class Photo(models.Model):
    # 사진 카테고리
    category = models.CharField(max_length=200, blank=True)
    # 사진 생성 일자
    created = models.CharField(max_length=50)
    # 이미지
    image = models.TextField()
    # 좌표 - left
    axis_left = models.FloatField(default=0.0)
    # 좌표 - top
    axis_top = models.FloatField(default=0.0)
    # 이미지와 관련된 상품 이미지
    product_image = models.TextField()
    # 상품 이미지의 id
    product_id = models.PositiveIntegerField(default=0)
    # 사진 글
    text = models.TextField(blank=True)
    # 작성자
    author = models.CharField(max_length=50)
    # 작성자의 프로필 이미지
    author_profile_image = models.TextField(blank=True)
    # 작성자의 프로필 글
    author_profile_comment = models.TextField(blank=True)
    # 좋아요 수
    like_count = models.PositiveIntegerField(default=0)
    # 스크랩 수
    scrap_count = models.PositiveIntegerField(default=0)
    # 조회 수
    hit_count = models.PositiveIntegerField(default=0)
    # 댓글 수
    comment_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "(" + self.author + ")" + self.text

    class Meta:
        ordering = ['id']

class Tag(models.Model):
    # 태그가 속한 사진
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='tags')
    # 태그 단어
    word = models.CharField(max_length=100)

    def __str__(self):
        return "#" + self.word

    class Meta:
        ordering = ['id']

class PhotoComment(models.Model):
    # 댓글이 속한 사진
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')
    # 댓글 작성자
    author = models.CharField(max_length=50)
    # 작성자의 프로필 이미지
    author_profile_image = models.TextField(blank=True)
    # 댓글 내용
    text = models.TextField()
    # 댓글 생성 일자
    created = models.CharField(max_length=50)

    def __str__(self):
        return "(" + self.author + ")" + self.text

    class Meta:
        ordering = ['id']

class Housewarming(models.Model):
    title = models.CharField(max_length=100)
    created = models.CharField(max_length=60)
    author = models.CharField(max_length=40)
    # 작성자의 프로필 글 url
    author_profile = models.TextField(blank=True)
    # 좋아요 수
    like_count = models.PositiveIntegerField(default=0)
    # 스크랩 수
    scrap_count = models.PositiveIntegerField(default=0)
    # 조회 수
    hit_count = models.PositiveIntegerField(default=0)
    # 커버 이미지
    cover_image = models.TextField()

    structure = models.CharField(max_length=50)
    floor_space = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    work = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    detail_part = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    # 댓글 수
    comment_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "(" + self.author + ")" + self.title

    class Meta:
        ordering = ['id']

class DetailContent(models.Model):
    housewarming = models.ForeignKey(Housewarming, on_delete=models.CASCADE, related_name='detail_contents')
    title = models.CharField(max_length=50, blank=True)
    image = models.TextField()
    text = models.TextField()


class HousewarmingComment(models.Model):
    # 댓글이 속한 사진
    housewarming = models.ForeignKey(Housewarming, on_delete=models.CASCADE, related_name='comments')
    # 댓글 작성자
    author = models.CharField(max_length=50)
    # 작성자의 프로필 이미지
    author_profile_image = models.TextField(blank=True)
    # 댓글 내용
    text = models.TextField()
    # 댓글 생성 일자
    created = models.CharField(max_length=50)

    def __str__(self):
        return "(" + self.author + ")" + self.text

    class Meta:
        ordering = ['id']


class HotStoryNumber(models.Model):
    # 랜덤 숫자를 위한 필드
    product_rnd_number = models.PositiveIntegerField(default=0)
    # 날짜 비교를 위한 필드
    updated = models.DateField(auto_now=True)

    def __str__(self):
        # 객체의 이름 - 랜덤 숫자
        return str(self.product_rnd_number)

    class Meta:
        ordering = ['id']

