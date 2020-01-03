from django.shortcuts import render, get_object_or_404
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from . import models
from . import serializers
from rest_framework import viewsets
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Talk, Projects, Algorithm, Skilltalk

# Create your views here.

#글 뷰셋
class TalkViewset(viewsets.ModelViewSet):
    queryset = models.Talk.objects.all()
    serializer_class = serializers.TalkSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = models.Projects.objects.all()
    serializer_class = serializers.ProjectSerializer

class AlgorithmViewset(viewsets.ModelViewSet):
    queryset = models.Algorithm.objects.all()
    serializer_class = serializers.AlgorithmSerializer

class SkilltalkViewset(viewsets.ModelViewSet):
    queryset = models.Skilltalk.objects.all()
    serializer_class = serializers.SkilltalkSerializer

#홈

def index(request):
    return render(request, 'index.html')


#댓글 뷰셋

class TalkCommentViewset(viewsets.ModelViewSet):
    queryset = models.TalkComment.objects.all()
    serializer_class = serializers.TalkCommentSerializer

    def get_queryset(self):
        post_id = self.kwargs["id"]
        queryset = models.TalkComment.objects.filter(post=post_id)
        return queryset



class ProjectCommentViewset(viewsets.ModelViewSet):
    queryset = models.ProjectsComment.objects.all()
    serializer_class = serializers.ProjectCommentSerializer
    def get_queryset(self):
        post_id = self.kwargs["id"]
        queryset = models.ProjectsComment.objects.filter(post=post_id)
        return queryset

class AlgorithmCommentViewset(viewsets.ModelViewSet):
    queryset = models.AlgorithmComment.objects.all()
    serializer_class = serializers.AlgorithmCommentSerializer
    def get_queryset(self):
        post_id = self.kwargs["id"]
        queryset = models.AlgorithmComment.objects.filter(post=post_id)
        return queryset

class SkilltalkCommentViewset(viewsets.ModelViewSet):
    queryset = models.SkilltalkComment.objects.all()
    serializer_class = serializers.SkilltalkCommentSerializer
    def get_queryset(self):
        post_id = self.kwargs["id"]
        queryset = models.SkilltalkComment.objects.filter(post=post_id)
        return queryset


@require_POST
@csrf_exempt
def like(request):
    if request.method == 'POST':
        ds = json.loads(request.body)
        title= ds['title']
        user = ds['userid']
        postid = ds['postid']

        post = Talk
        
        if title == 'talk':
            post = Talk.objects.get(id= postid)
        elif title == 'algorithm':
            post = Algorithm.objects.get(id= postid)
        elif title == 'projects':
            post = Projects.objects.get(id= postid)
        elif title == 'skilltalk':
            post = Skilltalk.objects.get(id= postid)
        else:
            raise Exception("올바른 주제 입력이 아닙니다")
        
        
        
        
        if post.likes.filter(id = user).exists():
            post.likes.remove(user)
            message = "좋아요가 취소되었습니다"
        else:
            post.likes.add(user)
            message = "이글을 좋아합니다"

    context = {'like_count' : post.total_likes, 'message': message}
    return HttpResponse(json.dumps(context), content_type='application/json')





