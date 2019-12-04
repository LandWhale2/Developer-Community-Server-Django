from django.shortcuts import render
from talk.models import Talk
from talk.serializers import TalkSerializer
from rest_framework import generics
# Create your views here.


class TalkList(generics.ListCreateAPIView):  
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer

#generics 에 상세 , 수정, 삭제 api 정의되어있다
class TalkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer