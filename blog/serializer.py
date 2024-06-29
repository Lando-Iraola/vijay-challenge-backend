from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    
    class Meta:
        model = User
        fields = {'id', 'username', 'posts'}