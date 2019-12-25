from django.shortcuts import render
from .serializers import UserSerializer, LoginSerializer, emailcheck
from django.http import HttpResponse
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from django.views import View
from django.utils.encoding import force_text
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from .models import User
import traceback
from rest_framework import viewsets
import re
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignIn(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if email and password:
            user_obj = User.objects.get(email = email, password= password)
            if user_obj:
                user = LoginSerializer(user_obj)
                data_list = {}
                data_list.update(user.data)
                return Response({"message": "로그인 성공", "data": data_list, "code": 200})
            else:
                message = "로그인 실패"
                return Response({"message": message, "code": 500, "data": {}})
        else:
            message = "올바르지않은 입력"
            return Response({"message": message, "code": 500, "data": {}})


class UserActivate(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk = uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        try:
            if user is not None and account_activation_token.check_token(user, token):
                user.active = True
                user.token = token
                user.save()
                return Response(user.email + '계정이 활성화되었습니다', status=status.HTTP_200_OK)
            else:
                return Response('만료된 링크입니다', status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(traceback.format_exc())


class EmailCheckView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = emailcheck(data=request.data)

        email = request.data.get('email', None)
        if serializer.is_valid():
            p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if p.match(email) is None:
                return Response('올바른 이메일 형식이 아닙니다', status=status.HTTP_400_BAD_REQUEST)
            return Response('사용가능한 이메일입니다', status=status.HTTP_200_OK)
        
        return Response('이미 존재하는 이메일 입니다', status=status.HTTP_400_BAD_REQUEST)



@require_POST
@csrf_exempt
def userupdate(request):
    if request.method == 'POST':
        ds = json.loads(request.body)
        token = ds['token']
        nickname = ds['nickname']

        
        

        if User.objects.filter(token = token).exists():
            user = User.objects.get(token= token)
            print(user)
            user.nickname = nickname
            print(user.nickname)
            message = '업데이트완료'
            data = user.nickname
            context = {'data' : data, 'message': message}
            return HttpResponse(json.dumps(context), content_type='application/json')
        else:
            message = '업데이트 실패'
            data = user.nickname
            context = {'data' : data, 'message': message}
            return HttpResponse(json.dumps(context), content_type='application/json')
        

        
    