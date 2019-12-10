from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets

# Create your views here.


class TalkViewset(viewsets.ModelViewSet):
    queryset = models.Talk.objects.all()
    serializer_class = serializers.TalkSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = models.Projects.objects.all()
    serializer_class = serializers.TalkSerializer

# class ProjectsViewset(viewsets.GenericViewSet):
#     queryset = models.Posts.objects.all()
#     serializer_class = serializers.ProjectsSerializer


# class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer

