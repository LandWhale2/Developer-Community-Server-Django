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


#댓글 serializer

class TalkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TalkComment
        fields = '__all__'

class ProjectCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectsComment
        fields = '__all__'

class AlgorithmCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlgorithmComment
        fields = '__all__'

class SkilltalkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SkilltalkComment
        fields = '__all__'