from django.db import models

# Create your models here.
class Base(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
# 用户表
class User(Base):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    img = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    is_active = models.IntegerField()
    level = models.IntegerField()
    integral = models.CharField(max_length=50)
    token = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'

# 第三方登录表
class ThirdPartyLogin(Base):
    user = models.ForeignKey('User', models.CASCADE)
    login_type = models.IntegerField()
    uid = models.CharField(max_length=30)


# 站内信表
class SiteMessage(Base):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=300)

# 用户---站内信表（UserSiteMessage）
class UserSiteMessage(Base):
    user = models.ForeignKey('User', models.CASCADE)
    sitemessage = models.ForeignKey('SiteMessage', models.CASCADE)
    status = models.IntegerField()

# 用户等级表
class UserLevel(Base):
    level = models.CharField(max_length=10)

# 用户等级条件表
class UserLevelCondition(Base):
    level = models.ForeignKey('UserLevel', models.CASCADE)
    time = models.IntegerField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)

# 有效用户表
class EffectiveMember(Base):
    user = models.ForeignKey('User', models.CASCADE)
    lever = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# 会员订单记录表
class MemberOrder():
    order_sn = models.CharField(max_length=50)
    user = models.ForeignKey('User', models.CASCADE)
    level = models.IntegerField()
    time = models.IntegerField()
    serical_number = models.CharField(max_length=50)
    status = models.IntegerField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    pay_type = models.IntegerField()
    code = models.CharField(max_length=50)

# 

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