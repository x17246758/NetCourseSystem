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



