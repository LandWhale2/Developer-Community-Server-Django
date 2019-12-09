from django.shortcuts import render
from posts.models import Posts
from posts.serializers import PostsSerializer
from rest_framework import generics

# Create your views here.


class PostsList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

