from django.contrib import admin
from django.db.models import Count
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _like_count=Count('likes', distinct=True),
            _comments_count=Count('comments', distinct=True),
        )
        return queryset

    list_display = (
        'id',
        'header',
        'author',
        'extra_field_total_likes',
        'extra_field_total_comments',
    )
    list_filter = search_fields = ('id', 'header', 'author',)

    def extra_field_total_likes(self, obj):
        return obj.total_likes()

    def extra_field_total_comments(self, obj):
        return obj.total_comments()

    extra_field_total_likes.short_description = 'Количесвто лайков'
    extra_field_total_comments.short_description = 'Количество комментариев'
    extra_field_total_likes.admin_order_field = '_like_count'
    extra_field_total_comments.admin_order_field = '_comments_count'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = list_filter = search_fields = (
        'id',
        'post',
        'author',
    )


admin.sites.AdminSite.empty_value_display = '-пусто-'
