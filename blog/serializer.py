from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False)
    content = serializers.CharField(required=True, allow_blank=False)
    author = serializers.CharField(required=True, allow_blank=False)
    created_at = serializers.DateTimeField(required=False, read_only=True)
    
    def create(self, validated_data):
        return Post.objects.create(validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance