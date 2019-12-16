from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets

# Create your views here.

#글 전용 뷰셋
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
