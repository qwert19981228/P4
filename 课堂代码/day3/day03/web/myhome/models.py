from django.db import models

# Create your models here.
class User(models.Model):
    
    # sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True)
    age = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=32,null=True)
    addtime = models.DateTimeField(auto_now=True,null=True)


    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name

class Wife(models.Model):
    wname = models.CharField(max_length=5)
     # 第一个参数：是被关联的模型名称
        # 第二个参数：当user用户表中的一条数据被删除的时候，与之对应的详情表数据也会被删除
    uid = models.OneToOneField(User, on_delete=models.CASCADE) # CASCADE是只一同删除

    def __str__(self):
        return self.wname

# 一对多
# 班级
class Class(models.Model):
    classname = models.CharField(max_length=32)


    def __str__(self):
        return self.classname

# 学员
class Stu(models.Model):
    sname = models.CharField(max_length=32)

    # 一对多
    cid = models.ForeignKey(to="Class", to_field="id")


    def __str__(self):
        return self.sname

# 多对多
class Classs(models.Model):
    classname = models.CharField(max_length=32)
    def __str__(self):
        return self.classname

class Teacher(models.Model):
    tname = models.CharField(max_length=32)
    cid = models.ManyToManyField(to="Classs")

    def __str__(self):
        return self.tname


