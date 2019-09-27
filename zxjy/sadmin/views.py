from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView,Response
# Create your views here.
from sadmin.serializers import *


#用户等级条件表
class UserLevelCondition(APIView):
    def post(self,request):
        mes={}
        data=request.data
        print(data)
        try:
            id=int(data['id'])
        except:
            id=0
        print(id)
        if id>0:
            cc=UserLevelCondition.objects.get(id=id)
            c=ULCSerializer(cc,data=data)
            #修改
        else:
            c = ULCSerializer(data=data)

        if c.is_valid():
            c.save()
            mes['code'] = 200
            mes['message'] = 'ok'
            print('ok')
        else:
            mes['code'] = 20010
            mes['message'] = '序列化失败'
            print(c.errors)

        return Response(mes)
