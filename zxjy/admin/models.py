from django.db import models

# Create your models here.
class Base(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(Base):
    pass

#角色表
class Roles(Base):
    name = models.CharField(max_length=50)
    status = models.IntegerField(default=1,verbose_name='状态，0停用，1启用')

    class Meta:
        db_table = 'roles'

#资源表
class Resources(Base):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=155,verbose_name='权限路由')
    status = models.IntegerField(default=1,verbose_name='状态，0停用，1启用')

    class Meta:
        db_table = 'resources'

#角色资源表
class RoleResource(Base):
    roles_id = models.IntegerField(default=0,verbose_name='角色ID')
    resources_id = models.IntegerField(default=0,verbose_name='资源ID')

    class Meta:
        db_table = 'role_resource'

#管理员表
class Admin(Base):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=188)
    roles = models.ForeignKey(Roles,on_delete=models.CASCADE)

    class Meta:
        db_table = 'admin'




#活动表
class Act(Base):
    title = models.CharField(max_length=50,verbose_name='活动标题')
    date = models.DateField(verbose_name='活动日期')
    content = models.TextField(verbose_name='活动内容描述')

    class Meta:
        db_table = 'act'

#秒杀时间表
class Time(Base):
    start = models.DateTimeField(verbose_name='活动开始时间')
    end = models.DateTimeField(verbose_name='活动结束时间')

    class Meta:
        db_table = 'time'

#秒杀产品表
class Sk(Base):
    act = models.ForeignKey(Act,on_delete=models.CASCADE)
    time = models.ForeignKey(Time,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=99999999.99,verbose_name='描述价格')

    class Meta:
        db_table = 'Sk'