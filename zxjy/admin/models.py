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

    class Meta:
        db_table = 'thirdpartylogin'


# 站内信表
class SiteMessage(Base):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=300)

    class Meta:
        db_table = 'sitemessage'


# 用户---站内信表（UserSiteMessage）
class UserSiteMessage(Base):
    user = models.ForeignKey('User', models.CASCADE)
    sitemessage = models.ForeignKey('SiteMessage', models.CASCADE)
    status = models.IntegerField()

    class Meta:
        db_table='usersitemessage'

# 用户等级表
class UserLevel(Base):
    level = models.CharField(max_length=10)

    class Meta:
        db_table = 'userlevel'

# 用户等级条件表
class UserLevelCondition(Base):
    level = models.ForeignKey('UserLevel', models.CASCADE)
    time = models.IntegerField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'userlevelconditon'

# 有效用户表
class EffectiveMember(Base):
    user = models.ForeignKey('User', models.CASCADE)
    lever = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        db_table = 'effectivemember'

# 会员订单记录表
class MemberOrder(Base):
    order_sn = models.CharField(max_length=50)
    user = models.ForeignKey('User', models.CASCADE)
    level = models.IntegerField()
    time = models.IntegerField()
    serical_number = models.CharField(max_length=50)
    status = models.IntegerField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    pay_type = models.IntegerField()
    code = models.CharField(max_length=50)

    class Meta:
        db_table = 'memberorder'


# 用户收藏实验问答报告表
class Collect(Base):
    user_id = models.IntegerField()  # 关联用户
    find_id = models.IntegerField()  # 关联实验问答或实验报告
    collect_tpye = models.IntegerField(default=0)  # 0:实验问答   1：实验报告

    class Meta:
        db_table = 'collect'

# 课程订单记录表
class Course_order(Base):
    order_sn = models.CharField(max_length=200)  # 订单编号
    user_id = models.IntegerField()             # 关联用户
    course_id = models.IntegerField()           # 关联课程
    pay_type = models.IntegerField(default=0)   # 支付方式  0：支付宝 1：微信  2：网银
    price = models.DecimalField(max_digits=10, decimal_places=2, default=9999999) # 价格
    pay_price = models.DecimalField(max_digits=10, decimal_places=2, default=9999999)  # 最终价格
    preferential_way = models.IntegerField(default=0)  # 优惠方式  0：不使用   1：优惠劵   2：积分
    referential_mone = models.DecimalField(max_digits=7, decimal_places=2, default=9999)  # 优惠金额
    order_status = models.IntegerField(default=0)  # 订单状态 ：是否评论 0：未评论  1：已评论
    code = models.CharField(max_length=200)  #  流水号
    coupon = models.CharField(max_length=200)  # 优惠劵码
    pay_sattus = models.IntegerField(default=0)  # 支付状态  0:未支付  1：已支付

    class Meta:
        db_table = 'course_order'

# 积分规则兑换表
class Rule(Base):
    ratio = models.FloatField(max_length=100)  #兑换比例

    class Meta:
        db_table = 'rule'

#  积分记录表
class Integral_record(Base):
    user_id = models.IntegerField()  # 关联用户表
    x_integral = models.IntegerField() # 操作类型 1：加   2：减
    s_integral  = models.IntegerField() # 操作前积分
    befrore_integral = models.IntegerField() # 本次操作积分
    end_integral  = models.IntegerField() # 操作后积分
    effect = models.IntegerField()  # 积分用途说明  0：抵扣现金  1：兑换优惠劵
    coupon_code = models.CharField(max_length=200)  # 积分详细说明

    class Meta:
        db_table = 'integral_record'

# 优惠劵表
class Coupon(Base):
    name = models.CharField(max_length=50) # 优惠劵名称，描述
    count = models.IntegerField()  # 优惠劵数量
    type = models.IntegerField()  # 类型： 0:首次注册会员  1：通用  2：指定商品  3：指定会员等级
    course_id = models.IntegerField(null=True)  #类型为2时关联课程
    start_time = models.DateTimeField(auto_now_add=True) # 创建开始日期
    end_time = models.DateTimeField() # 创建结束日期
    status = models.IntegerField(default=0)  # 0:可用  1：过期或停用
    condition = models.DecimalField(max_digits=7,decimal_places=2,default=9999)  # 减免条件
    money = models.DecimalField(max_digits=7,decimal_places=2,default=10)  # 优惠劵金额

    class Meta:
        db_table = 'coupon'

# 用户优惠劵表
class User_Coupon(Base):
    user_id = models.IntegerField()  # 关联用户
    count = models.CharField(max_length=50,unique=True)  # 优惠劵唯一编码
    start_time = models.DateTimeField(auto_now_add=True)  # 优惠劵开始日期
    end_time = models.DateTimeField()  # 优惠劵结束日期
    condition = models.DecimalField(max_digits=7, decimal_places=2, default=9999)  # 减免条件
    money = models.DecimalField(max_digits=7, decimal_places=2, default=10)  # 优惠劵金额
    is_use = models.IntegerField(default=0) #是否使用 0：未使用  1：使用

    class Meta:
        db_table = 'user_coupon'



#学习记录表
class User_course(Base,models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)   #关联课程一对多
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)       #关联用户一对多
    section_id = models.ForeignKey('Section', on_delete=models.CASCADE) #关联章节一对多
    status = models.IntegerField(default=0)  # 完成状态（0，未完成，1完成）
    class Meta:
        db_table = 'user_course'

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





class Path(Base,models.Model):
    pic = models.CharField(max_length=225)
    path = models.CharField(max_length=50)
    info = models.CharField(max_length=220)
    studynum = models.IntegerField()
    class Meta:
        db_table = 'Path'


# 阶段表
class Path_stage(Base,models.Model):
    stage_name = models.CharField(max_length=100)
    path = models.ForeignKey(Path,models.CASCADE)
    sort = models.IntegerField()
    class Meta():
        db_table = 'Path_stage'


#课程标签
class Tags(Base,models.Model):
    name = models.CharField(max_length=50)
    class Meta():
        db_table = 'Tags'

#  讲师表
class Teacher(Base, models.Model):
    name = models.CharField(max_length=10)  # 讲师名称
    describe = models.CharField(max_length=50)  # 讲师描述
    pic = models.CharField(max_length=100)  # 讲师头像

    class Meta:
        db_table = "teacher"

# 课程表
class Course(Base,models.Model):
    title = models.CharField(max_length=50)
    pic = models.CharField(max_length=220)
    info = models.CharField(max_length=220)
    omline = models.IntegerField(default=0)    #是否上线  0没上线 1上线
    member = models.IntegerField(default=0)    #是否会员  0非会员 1会员 2训练营
    attention = models.IntegerField()     #关注数
    learn = models.IntegerField()         #学过人数
    teacher = models.ForeignKey('Teacher',models.CASCADE)
    comment_num = models.IntegerField()    #评论数
    path = models.ForeignKey(Path,models.CASCADE)
    tag = models.ForeignKey(Tags,models.CASCADE)
    recommand = models.CharField()         #课程推荐
    detail = models.CharField()
    section_num = models.IntegerField()    #章节数
    class Meta:
        db_table = 'Course'


#章节表
class Section(Base,models.Model):
    course = models.ForeignKey('Course',models.CASCADE)
    section = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    video = models.CharField(max_length=220)
    sort = models.IntegerField()   #排序
    class Meta:
        db_table = 'Section'


# 价格表
class Price(Base,models.Model):
    type = models.IntegerField()    #（普通/会员/高级会员）
    course = models.ForeignKey(Course,models.CASCADE)
    discount = models.FloatField()       #折扣
    discoun_price = models.DecimalField(max_digits=6,decimal_places=2)   #折扣价
    class Meta:
        db_table = 'Price'


# 用户关注表
class UserTeacher(Base, models.Model):
    user_id = models.ForeignKey('User', to_field='id', on_delete=models.CASCADE)  # 关联用户表
    teacher_id = models.ForeignKey('Teacher', to_field='id', on_delete=models.CASCADE)  # 关联讲师表

    class Meta:
        db_table = "userteacher"



# 实验报告表
class Report(Base, models.Model):
    section_id = models.ForeignKey('Section', to_field='id', on_delete=models.CASCADE)  # 关联章节表
    user_id = models.ForeignKey('User', to_field='id', on_delete=models.CASCADE)  # 关联用户表
    report_content = models.CharField(max_length=100)  # 报告内容
    report_title = models.CharField(max_length=20)  # 报告标题
    report_trowse = models.IntegerField(default=0)  # 实验报告浏览量
    linknum = models.IntegerField(default=0)  # 点赞数
    course_id = models.ForeignKey('Course', to_field='id', on_delete=models.CASCADE)  # 关联课程表
    class Meta:
        db_table = 'report'


# 实验问答表
class Answer(Base, models.Model):
    course_id = models.ForeignKey('Course', to_field='id', on_delete=models.CASCADE)  # 关联课程表
    answer_title = models.CharField(max_length=10)  # 问题标题
    answer_content = models.CharField(max_length=100)  # 问题内容
    browse_id = models.IntegerField(default=0)  # 浏览量
    user_id = models.ForeignKey('User', to_field='id', on_delete=models.CASCADE)   # 用户表关联
    pid = models.IntegerField(default=0)  # 上一级评论id
    top = models.IntegerField(default=0)  # 顶级评论id
    type_id = models.IntegerField(default=0)  # 自身级别id
    class Meta:
        db_table = 'answer'


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
    act = models.ForeignKey('Act', models.CASCADE)

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