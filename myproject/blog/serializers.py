from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'summary', 'is_archived', 'created_at', 'updated_at', 'comments_count']


    def get_comments_count(self, obj):
        return obj.comments.count()


    def validate_content(self, value):
        if len(value) < 50:
            raise serializers.ValidationError("Post content must contain at least 50 characters")
        return value
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at', 'updated_at']