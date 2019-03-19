from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
# def index(request):
#     return render(request,'myhome/index.html')

def dataAdd(request):
    # 数据的增删该查
    # 数据的添加
        # ob = models.User()
        # ob.name='zhasngan'
        # ob.age=20
        # ob.email='zhasnagn@qq.com'
        # ob.password='123456'
        # ob.save()

        # data={'name':'lisi','age':18,'email':'lisi@qq.com','password':'123456'}
        # ob = models.User(**data)
        # ob.save()
    # 删除数据
    # obs = models.User.objects.all()
    # obs = models.User.objects.filter(age=18)
    # obs = models.User.objects.get(age=20)

    # 这是字段查询 filter()、exclude()、get()的都可以实现where 下文filter也可以exclude
    # 我们在这里给学员减压 就是要filter
    # obs = models.User.objects.filter(name__contains='i')

    # 比较运算符
    # obs = models.User.objects.filter(age__lt=20)
    # obs.delete()

    # 更新数据
    obs = models.User.objects.get(id=1)
    obs.name='ss'
    obs.save()

    print(obs)
   
    return HttpResponse('数据模型操作')


# =========================
def index(request):
    return render(request,'myhome/index.html')

def addpage(request):
    return render(request,'myhome/add.html')

def addData(request):
    # 接受用户数据
    data = request.GET.dict()
    data['age']=int(data['age'])
    print(data)
    ob = models.User(**data) ## ** 意思是不定长的关键字参数
    ob.save()
    return HttpResponse('数据添加成功')

def select(request):
    # 获取数据
    ob = models.User.objects.all()

    return render(request,'myhome/select.html',{'info':ob})

def delData(request,uid):
    # 删数据
    ob = models.User.objects.get(id=uid)
    ob.delete()
    return HttpResponse('删除成功')
    