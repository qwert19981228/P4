from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse
from . import models
# 密码相关
from django.contrib.auth.hashers import make_password

# Create your views here.

def  index(request):
    return render(request,'myadmin/user/index.html')

def  useradd(request):
    # request.method
    # get 展示页面
    if request.method=='GET':
        return render(request,'myadmin/user/add.html')
    elif request.method=='POST':
        # post 提交表单 存入数据库
        
        # 接收post
        data = request.POST.dict()
        # 去除csrfmiddlewaretoken 
        data.pop('csrfmiddlewaretoken')

        # 密码加密
        # from django.contrib.auth.hashers import make_password
        # make_password(data['password'],None,'pbkdf2_sha256')
        data['password'] = make_password(data['password'],None,'pbkdf2_sha256')

        # 判断上传的头像
        # myfile = request.FILES.get("pic_url")
        # 判断 myfile的值
        # if myfile:
        #     # 执行上传
        #     # 明天讲解封装upload
            
        # else:
        
        data['pic_url'] = '/static/pics/user.png'

        print(data)

        # data 构建完毕 请求插入
        ob = models.Users(**data)
        ob.save()


        return HttpResponse('添加成功')

        


# 用户列表
def userlist(request):
    # 得到用户数据
    data = models.Users.objects.all()
    return render(request,'myadmin/user/userlist.html',{"info":data})

