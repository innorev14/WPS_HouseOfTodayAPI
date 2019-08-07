from django.contrib import admin
from .models import *


class PhotoAdmin(admin.ModelAdmin):
    fields = ['category', 'created', 'image', 'axis_left', 'axis_top',
              'product_image', 'product_id', 'text', 'author', 'author_profile_image',
              'author_profile_comment', 'like_count', 'scrap_count', 'hit_count', 'comment_count']
    list_display = ['id', 'author', 'text']


class TagAdmin(admin.ModelAdmin):
    fields = ['photo', 'word']
    list_display = ['id', 'word']


class PhotoCommentAdmin(admin.ModelAdmin):
    fields = ['photo', 'author', 'author_profile_image', 'text', 'created']
    list_display = ['id', 'author', 'text', 'created']


class HousewarmingAdmin(admin.ModelAdmin):
    fields = ['title', 'created', 'author', 'author_profile_image', 'author_profile_comment', 'like_count',
              'scrap_count', 'hit_count', 'cover_image', 'structure', 'floor_space', 'style', 'work', 'area',
              'period', 'budget', 'family', 'detail_part', 'location', 'comment_count']
    list_display = ['id', 'title', 'created', 'author']


class DetailContentAdmin(admin.ModelAdmin):
    fields = ['housewarming', 'title', 'image', 'text']
    list_display = ['id', 'housewarming', 'title', 'image', 'text']


class HousewarmingCommentAdmin(admin.ModelAdmin):
    fields = ['housewarming', 'author', 'author_profile_image', 'text', 'created']
    list_display = ['id', 'housewarming', 'author', 'author_profile_image', 'text', 'created']


class HotStoryNumberAdmin(admin.ModelAdmin):
    fields = ['product_rnd_number']
    list_display = ['id', 'product_rnd_number', 'updated']


# CronTab 로그 기록 Admin
class CronLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'cronjob_comment', 'cron_date']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PhotoComment, PhotoCommentAdmin)
admin.site.register(Housewarming, HousewarmingAdmin)
admin.site.register(DetailContent, DetailContentAdmin)
admin.site.register(HousewarmingComment, HousewarmingCommentAdmin)
admin.site.register(HotStoryNumber, HotStoryNumberAdmin)
admin.site.register(CronLog, CronLogAdmin)
