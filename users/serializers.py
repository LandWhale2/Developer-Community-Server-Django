from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from rest_framework import serializers
from .models import User
from .tokens import account_activation_token
import datetime
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    # created_by = serializers.CharField(max_length=64, required=False)
    # updated_by = serializers.CharField(max_length=64, required=False)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = '__all__'

    def to_internal_value(self, data):
        #POST/PUT 과 같이 데이터변경이있을떄 데이터 저장하기 전에 핸들링 가능한 함수
        ret = super(UserSerializer, self).to_internal_value(data)

        # cipher = AESSipher()
        # ret['password'] = cipher.encrypt_str(ret['password'])

        return ret
    
    def to_representation(self, obj):
        #GET/POST/Put 과 같이 데이터 변경이있고 그이후 data로 접근할떄 값을 변환하여 보여줍니다
        ret = super(UserSerializer, self).to_representation(obj)
        return ret
    
    def validate_email(self, value):
        #이메일이 데이터베이스에 존재하는지 확인함
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이메일이 이미 존재합니다")
        return value

    def validate_password(self, value):
        #패스워드 8자 이하
        if len(value) < 8:
            raise serializers.ValidationError("패스워드는 최소 %s 자 이상이어야합니다 " % 8)
        return value

    def create(self, validate_data):
        #데이터 저장할때 필요한 과정을 구현합니다
        user = User.objects.create(
            email = validate_data['email'],
            password = validate_data['password'],
            nickname = validate_data['nickname'],
        )
        
        
        user.active = False
        user.save()

        message = render_to_string('user/account_activate_email.html', {
            'user': user,
            'domain' : 'ec2-15-164-211-101.ap-northeast-2.compute.amazonaws.com:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })

        #이메일 전송 과정

        mail_subject = '회원가입 확인메일 입니다.'
        to_email = user.email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        return validate_data



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        


class emailcheck(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)
    
    def validate_email(self, value):
        #이메일이 데이터베이스에 존재하는지 확인함
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이메일이 이미 존재합니다")
        return value