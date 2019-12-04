from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bbs.models import Bbs
from bbs.serializers import BbsSerializer
# Create your views here.


#serializer 를 이용해서 웹으로부터 받을 view 파일을 작성, url 에서 bbs/ 로 끝나는 요청이 GET 일 경우 '목록' 으로 처리하고 POST 로 들어오면 '입력'으로 처리함.
#bbs/ 다음에 숫자값으로 입력되어있을경우 ex) bbs/22 에 GET 일 경우에 한개의 데이터 , PUT 은 수정, DELELTE 는 삭제처리를 수행한다 . 

# 요청 url 인 bss/ 에서 urls.py 에 정의된 view.bbs_list가 호출된다.
@api_view(['GET', 'POST'])
def bbs_list(request, format=None):
    if request.method == 'GET':
        bbs = Bbs.objects.all()
        serializer = BbsSerializer(bbs, many=True)#many값이 true 이면 다수의 데이터를 instance 직렬화 할수있다
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BbsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#요청 url인 bbs/번호 에 대해서 urls.py에 정의된 view.bbs_detail 이 호출된다


@api_view(['GET', 'PUT', 'DELETE'])
def bbs_detail(request, pk, format=None):
    try:
        bbs= Bbs.objects.get(pk=pk)
    except Bbs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BbsSerializer(bbs)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BbsSerializer(bbs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bbs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)