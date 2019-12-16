from django.shortcuts import render
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework import status, permissions
from django.views import View
from django.utils.encoding import force_text
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from .models import User
import traceback
# Create your views here.


class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignIn(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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