from django.db import models

# Create your models here.
# 创建一个User 类 
# 就是 User表
class User(models.Model):
    # 函数体 写上你的字段
    # 字段名 字段属性
    name = models.CharField(max_length=50,null=True)
    age = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50,null=True)
    # 加一个字段  auto_now 自动拿当前时间
    addtime = models.DateTimeField(auto_now=True,null=True)
    
    class Meta():
        # 设置表名
        db_table = 'users'

    def __str__(self):
        # 返回  以name 去返回  在后台管理中常用
        return self.name

# 分配老婆
# 生成一个 wife表
class Wife(models.Model):
    wname = models.CharField(max_length=50)
    # OneToOneField参数一 模型 参数二 是否关联删除. 主删除了,副也删除
    # 但是, 副删除了,主还在
    
    uid = models.OneToOneField(User,on_delete=models.CASCADE)  # 外键用户的id  表示属于谁的老婆

    def __str__(self):
        # 返回  以name 去返回  在后台管理中常用
        return self.wname


# 一对多
# 班级 一类
class Class(models.Model):
    classname = models.CharField(max_length=50)

    def __str__(self):
        # 返回  以name 去返回  在后台管理中常用
        return self.classname

# 学生 多类
class Stu(models.Model):
    sname = models.CharField(max_length=50)
    # 一对多 ForeignKey
    # 参数1 对应类 模型
    # 参数2 对应 字段
    cid = models.ForeignKey(to="Class",to_field='id')
    def __str__(self):
        # 返回  以name 去返回  在后台管理中常用
        return self.sname

# 多对多 

class Classes(models.Model):
    classname = models.CharField(max_length=50)

    def __str__(self):
        # 返回  以name 去返回  在后台管理中常用
        return self.classname

class Teacher(models.Model):
    tname = models.CharField(max_length=50)
    # 多对多 ManyToManyField
    # 会生成 第三张表- 关联表
    cid = models.ManyToManyField(to="classes")

    def __str__(self):
        # 返回  以name 去返回  在后台管理中常用
        return self.tname

