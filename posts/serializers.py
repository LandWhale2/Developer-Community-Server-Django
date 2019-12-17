from rest_framework import serializers
from . import models

#글 게시물serializer

class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Talk
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = '__all__'

class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Algorithm
        fields = '__all__'

class SkilltalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skilltalk
        fields = '__all__'