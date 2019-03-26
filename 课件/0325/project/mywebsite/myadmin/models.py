from django.db import models

# Create your models here.
class Users(models.Model):
    # 会员 
    # 姓名 密码 手机号 邮箱 性别 年龄 pic_url(头像地址) 状态 注册时间
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100,null=True)
    sex = models.CharField(max_length=1,choices=(('1','男'),('0','女')))
    age = models.IntegerField()
    pic_url = models.CharField(max_length=255)
    status = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True)





    