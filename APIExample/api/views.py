from rest_framework.views import APIView ,Response
from api.serializers import PostSerializer
from blogapp.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.viewsets import ModelViewSet
class PostListAPIView(APIView):
    def get(self,request):
        posts=Post.objects.all()
        serializers=PostSerializer(posts,many=True)
        return Response(serializers.data)
class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly,IsAuthenticatedOrReadOnly]

"""class PostAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['author','title']
    search_fields=['title','author__username']
    ordering_fields=['title','author__username']
"""
