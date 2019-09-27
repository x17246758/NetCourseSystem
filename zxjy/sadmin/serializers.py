from rest_framework import serializers
from sadmin.models import *


#
# class CateModelSerializer(serializers.ModelSerializer):  # 序列化 python 变json
#     class Meta:
#         model = Cate
#         fields = '__all__'


class ULCSerializer(serializers.Serializer):
    level_id= serializers.IntegerField()
    time = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=7, decimal_places=2)


    # 添加
    def create(self, data):  # data为前台页面传递的参数
        u = UserLevelCondition.objects.create(**data)
        return u

    #修改
    def update(self, instance, validated_data):
        # 修改参数
        instance.time = int(validated_data['time'])
        instance.level_id = int(validated_data.get('level_id'))
        instance.amount = validated_data.get('amount')
        instance.save()
        return instance