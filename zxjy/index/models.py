from django.db import models

# Create your models here.

# 路径表()
class Path(models.Model):
    pic = models.CharField(max_length=225)
    path = models.CharField(max_length=50)
    info = models.CharField(max_length=220)
    studynum = models.IntegerField()
    class Meta:
        db_table = 'Path'


# 阶段表
class Path_stage(models.Model):
    stage_name = models.CharField(max_length=100)
    path = models.ForeignKey(Path,models.CASCADE)
    sort = models.IntegerField()
    class Meta():
        db_table = 'Path_stage'


#课程标签
class Tags(models.Model):
    name = models.CharField(max_length=50)
    class Meta():
        db_table = 'Tags'


# 课程表
class Course(models.Model):
    title = models.CharField(max_length=50)
    pic = models.CharField(max_length=220)
    info = models.CharField(max_length=220)
    omline = models.IntegerField(default=0)    #是否上线  0没上线 1上线
    member = models.IntegerField(default=0)    #是否会员  0非会员 1会员 2训练营
    attention = models.IntegerField()     #关注数
    learn = models.IntegerField()         #学过人数
    teacher = models.ForeignKey()
    comment_num = models.IntegerField()    #评论数
    path = models.ForeignKey(Path,models.CASCADE)
    tag = models.ForeignKey(Tags,models.CASCADE)
    recommand = models.CharField()         #课程推荐
    detail = models.CharField()
    section_num = models.IntegerField()    #章节数
    class Meta:
        db_table = 'Course'


#章节表
class Section(models.Model):
    course = models.ForeignKey('Course',models.CASCADE)
    section = models.CharField(max_length=50)
    video = models.CharField(max_length=220)
    sort = models.IntegerField()   #排序
    class Meta:
        db_table = 'Section'


# 价格表
class Price(models.Model):
    type = models.IntegerField()    #（普通/会员/高级会员）
    course = models.ForeignKey(Course,models.CASCADE)
    discount = models.FloatField()       #折扣
    discoun_price = models.DecimalField(max_digits=6,decimal_places=2)   #折扣价
    class Meta:
        db_table = 'Price'














