from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from app01 import models
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from app01.serializer import *
# Create your views here.
from rest_framework import serializers

def reg(request):
    password = make_password('123456')
    admin = models.Sadmin(username='yy', password=password, is_admin=1)
    admin.save()
    return HttpResponse('ok')


class LoginView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        print(username)
        user = models.Sadmin.objects.filter(username=username).first()
        print(user)
        mes = {}
        if not user:
            mes['code'] = 10010
            mes['message'] = '用户不存在'
        else:
            if not check_password(password, user.password):
                mes['code'] = 10010
                mes['message'] = '密码错误'
            else:
                mes['code'] = 200
                mes['msg'] = '登录成功'
                mes['user'] = username
        return Response(mes)