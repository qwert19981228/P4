from django.db import models

# Create your models here.
# 创建一个User类
class User(models.Model):
    # 函数体 写上你的字段
    # 字段名 字段属性
    name = models.CharField(max_length=50,null=True)
    age = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50,null=True)

    class Meta():
        # 设置表名
        db_table = 'users'
    def __str__(self):
        # 返回 以name 去返回 在后台管理中常用
        return self.name

class Wife(models.Model):
    wname = models.CharField(max_length=50)
    uid = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        # 返回 以name 去返回 在后台管理中常用
        return self.wname

# 一对多
class Class(models.Model):
    classname = models.CharField(max_length=50)

    def __str__(self):
        # 返回 以name 去返回 在后台管理中常用
        return self.classname


class Stu(models.Model):
    sname = models.CharField(max_length=50)

    cid = models.ForeignKey(to='Class',to_field='id')
    def __str__(self):
        # 返回 以name 去返回 在后台管理中常用
        return self.sname

# 多对多

class Classes(models.Model):
    classname = models.CharField(max_length=50)

    def __str__(self):
        # 返回 以name 去返回 在后台管理中常用
        return self.classname

class Teacher(models.Model):
    tname = models.CharField(max_length=50)
    # 多对多 ManyToManyField
    # 会生成 第三张表 - 关联表
    cid = models.ManyToManyField(to="classes")

    def __str__(self):
        # 返回 以name去返回 在后台管理中常用
        return self.tname