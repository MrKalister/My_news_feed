from rest_framework import serializers

from posts.models import Comment, Post

COUNT_COMMENTS = 10


class AbstractBaseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    created_date = serializers.DateTimeField(
        format='%d.%m.%Y, %H:%M', read_only=True)


class CommentSerializer(AbstractBaseSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'created_date')
        model = Comment


class CreatePostSerializer(AbstractBaseSerializer):
    """Return resulat after create a object."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    created_date = serializers.DateTimeField(
        format='%d.%m.%Y, %H:%M', read_only=True)

    class Meta:
        fields = ('id', 'header', 'text', 'author', 'created_date')
        model = Post


class GetPostSerializer(CreatePostSerializer):
    total_likes = serializers.ReadOnlyField()
    total_comments = serializers.ReadOnlyField()
    last_comments = serializers.SerializerMethodField()

    @staticmethod
    def get_last_comments(obj):
        return [CommentSerializer().to_representation(text) for text in
                obj.comments.all().order_by('-created_date')[:COUNT_COMMENTS]]

    class Meta(CreatePostSerializer.Meta):
        fields = CreatePostSerializer.Meta.fields + (
            'last_comments', 'total_likes', 'total_comments')
