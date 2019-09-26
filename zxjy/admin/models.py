from django.db import models

# Create your models here.
class Base(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(Base):
    pass

#学习记录表
class User_course(Base,models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)   #关联课程一对多
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)       #关联用户一对多
    section_id = models.ForeignKey('Section', on_delete=models.CASCADE) #关联章节一对多
    status = models.IntegerField(default=0)  # 完成状态（0，未完成，1完成）

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
