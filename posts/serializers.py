from rest_framework import serializers
from . import models

#글 게시물serializer

class TalkSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url = True, required=False)
    class Meta:
        model = models.Talk
        fields = ('content','image', 'title', 'created', 'writer', 'id')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url = True, required=False)
    class Meta:
        model = models.Projects
        fields = ('content','image', 'title', 'created', 'writer', 'id')

class AlgorithmSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url = True, required=False)
    class Meta:
        model = models.Algorithm
        fields = ('content','image', 'title', 'created', 'writer', 'id')

class SkilltalkSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url = True, required=False)
    class Meta:
        model = models.Skilltalk
        fields = ('content','image', 'title', 'created', 'writer', 'id')


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