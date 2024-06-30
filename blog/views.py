from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from django.http import Http404
from .models import Post
from .models import Post
from .serializer import PostSerializer
from .serializer import UserSerializer
from django.contrib.auth.models import User

# Create your views here.


class PostView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    @csrf_exempt
    def get(self, request, format=None):
        posts = Post.objects.all()
        
        paginator = PageNumberPagination()
        paginator.page_size = 6
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        print(request.data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    @csrf_exempt
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer