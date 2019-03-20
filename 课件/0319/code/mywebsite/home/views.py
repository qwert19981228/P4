from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse
from . import models
# Create your views here.


def index(request):
    return render(request,'home/index.html') # 通过http去打开 一个index.html

# 数据的增删改查
def dataAdd(request):
    # 数据添加
    # ob = models.User()# 得到数据库 user类
    # 准备好数据 
    # ob.name = '小娜'
    # ob.age = 18
    # ob.email = '123@qq.com'
    # ob.password = '123456'
    # # 往 user中插入
    # # save 方法  保存
    # ob.save()
    # 一条搞定 key-values形式
    # data = {'name':'连楷','age':20,'email':'liankai@163.com','password':'123456'}
    # ob = models.User(**data)
    # ob.save()

    # 删除数据
    # 知道 删除哪些数据 
    # 再去执行删除
    
    #查询
    # obs = models.User.objects.all()
    # obs = models.User.objects.filter(age=16)  # 条件 获取所有符合条件
    #获取单条get
    # obs = models.User.objects.get(age=16)  # 条件
    # obs = models.User.objects.get(age=18)  # 条件 查询到2条会报错
    # 包含字符串
    # obs = models.User.objects.filter(name__contains='飞')  # 条件
    # 范围查看
    # obs = models.User.objects.filter(age__lt=18)  # 条件
    
    # obs.delete() # 把obs 中的结果全部删除 有几个删除几个

    # 更新数据
    # 改谁   连楷
    # 改什么  连连看
    # 执行修改  sql
    
    # 查询
    obs = models.User.objects.get(id=4)  # 条件
    # obs 是 连楷 这个对象
    # 里面有  name  age  sex  eamil password
    obs.name = '连连看'  # 赋值name
    obs.save()

    print(obs)


    return HttpResponse('数据的增删改查')


# 展示表单页面
def addpage(request):
    return render(request,'home/add.html')

# 执行添加的表单请求
def add(request):
    # 接收get参数 request.GET.dict()
    data = request.GET.dict()
    data['age'] =int(data['age']) # int 转换 年龄
    print(data)
    ob = models.User(**data)
    ob.save()
    
    return HttpResponse('添加成功了,哥哥')

# 展示学生列表(重点)
# 把数据交给页面 使用render 方法 第三个参数 
def userlist(request):
    # 查询所有
    ob = models.User.objects.all()
    print(ob)

    return render(request,'home/list.html',{'info':ob})
    # 第三个参数 把ob 放入 info中
    # 一起 给 这个页面
    # return render(request,'home/list.html')

# 删除操作
def delUser(request,uid):
    # 删除操作
    # 查询 uid 这条数据
    ob = models.User.objects.get(id=uid)
    # 执行删除
    ob.delete()
    return HttpResponse('删除成功了,小哥哥')



#========================================================
# 视图是以函数为载体的.
# def index(request):
#     return HttpResponse('hello') # 通过http去响应 响应信息 就是 hello


# def abc(request):
#     return HttpResponse('efg') # 通过http去响应 响应信息 就是 hello


# #响应页面
# def page(request):
#     return render(request,'index.html')  # 会直接找 定义好的 模板位置 + 路径名


# #位置参数  需要你定义个  变量 收一下哎 
# #这里变量名字 不做限制
# def title(request,year):
#     return HttpResponse('参数我收到啦'+year)

# #关键字传参
# ##这里变量名字 有限制
# #跟url定义的 关键字对上
# # def guan_title(request,month): 这里会报错 提示 没有year这个坑位
# def guan_title(request,year):
#     return HttpResponse('关键字参数我收到啦'+year)


# #默认值传参
# def detail(request,year='2020'):
#     return HttpResponse('我是默认参数的处理'+year)


# # 反向解析  reverse('url名字')
# def turnover(request):
#     print(reverse('over'))   # 会直接打印在 控制台(cmder)
#     print(reverse('fall'))   # 会直接打印在 控制台(cmder)
#     # path = reverse('over')  # 如果自己 跳自己  那就 爱的魔力转圈圈
#     path = reverse('fall')
#     return HttpResponse('<script>location.href="'+path+'"</script>')


# # 接着昨天没讲的反向解析带参数

# def fall(request):
#     path = reverse("title", args=("2020", ))
#     print(path)  # title/2020
#     return HttpResponse('我坠入爱河了')


def page_not_found(request):
    return render(request, '404.html')
     
     
def page_error(request):
    return render(request, 'project_error/500.html')
     
     
def permission_denied(request):
    return render(request, 'project_error/403.html')