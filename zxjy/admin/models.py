from django.db import models

# Create your models here.
class Base(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(Base):
    pass

<<<<<<< HEAD
#学习记录表
class User_course(Base,models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)   #关联课程一对多
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)       #关联用户一对多
    section_id = models.ForeignKey('Section', on_delete=models.CASCADE) #关联章节一对多
    status = models.IntegerField(default=0)  # 完成状态（0，未完成，1完成）
=======
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
>>>>>>> 8acad9354fadb49694123dcb590c3cc20cf71d49

    class Meta:
        db_table = 'user_coures'

#评论表
class Comment(Base,models.Model):
    content = models.CharField(max_length=255,name='评论内容')
    pid = models.IntegerField(default=0,name='上级评论id')
    top_id = models.IntegerField(default=0,name='顶级评论id')
    type_id = models.IntegerField(default=0,name='自身级别id')
    user_id = models.ForeignKey('User',on_delete=models.CASCADE)        #用户外键
    course_id = models.ForeignKey('Course',on_delete=models.CASCADE)    #课程外键
    comment_type = models.CharField(max_length=100,name='评论类型')
    status = models.IntegerField(default=0,name='审核状态')              #(0是通过，1是不通过)
    reason = models.CharField(max_length=255,name='失败原因')

    class Meta:
        db_table = 'comment'


<<<<<<< HEAD
#焦点图表
class Banner(Base,models.Model):
    name = models.CharField(max_length=255,name='图片名称')
    pic = models.CharField(max_length=255,name='图片')          
    url = models.CharField(max_length=255,name='跳转链接')      #点击图片跳转链接
    type = models.IntegerField(default=1,name='类型')           #(1，首页，2课程，3路径，4训练营)
    is_show = models.IntegerField(default=1,name='是否显示')    #(1,显示，2,不显示)
    sort = models.IntegerField(default=1,name='排序')       

    class Meta:
        db_table = 'banner'
=======

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
>>>>>>> 8acad9354fadb49694123dcb590c3cc20cf71d49
