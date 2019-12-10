from rest_framework import serializers
from . import models

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Talk
        fields = ('id', 'content')

class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Talk
        fields = ('id', 'content', 'title')