from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message
from users.models import User
from chat.serializers import MessageSerializer
from users.serializers import UserSerializer




# 채팅 유저 목록
@csrf_exempt
def user_list(request, pk=None):
    if request.method == 'GET':
        if pk: # pk 를 기준으로 특정한 유저를 Return
            users = User.objects.filter(id=pk)
        else: #그외의 경우엔 전체 유저를 Return 해줌
            users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request}) 
        return JsonResponse(serializer.data, safe=False)


#해당하는 유저와의 채팅 메세지 리스트
@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET': # 메세지 리스트
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
        messages2 = Message.objects.filter(sender_id=receiver, receiver_id=sender)
        allmessage = messages | messages2
        serializer = MessageSerializer(allmessage, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST': #메세지 전송
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)