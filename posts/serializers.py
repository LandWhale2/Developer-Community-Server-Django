from rest_framework import serializers
from . import models

#글 게시물serializer

class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Talk
        fields = ('id', 'content', 'title', 'created')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = ('id', 'content', 'title', 'created')

class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Algorithm
        fields = ('id', 'content', 'title', 'created')

class SkilltalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skilltalk
        fields = ('id', 'content', 'title', 'created')