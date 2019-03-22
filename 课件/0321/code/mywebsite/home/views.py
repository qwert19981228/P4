from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse
from . import models
# Create your views here.


# def index(request):
#     return render(request,'home/index.html') # 通过http去打开 一个index.html



# 重定向讲解
# 引入 redirect
# rediect(url)
def index(request):
    # 访问到这里
    # 重定向到  reindex
    # return HttpResponse('我是跳的')
    # 得到重定向的路由
    path = reverse('home_reindex')

    # return HttpResponse('<script>location.href="'+path+'"</script>')
    # return redirect(path)
    # return redirect('reindex/')
    return redirect(reverse('home_reindex'))

# 重定向跳转的url
def reindex(request):
    return HttpResponse('我是重定向')


# request
# request 带来什么东西
def url_path(request):
    print(request) # 得到对象
    # 得到 path
    print(request.path)
    # 得到 method
    print(request.method)

    print('========================')
    # 得到 GET 参数
    print(request.GET)
    # print(request.GET['id'])
    # print('======dict==================')

    # print(request.GET.dict())
    # print('=======list=================')
    # # 获取一段list
    # print(request.GET.getlist('id'))
    print('=======get id=================')

    print(request.GET.get('id'))
    # 默认值10
    print(request.GET.get('id',10))

    
    return HttpResponse('皇上,臣妾是夏雨荷')


# request 上传
# 处理上传的参数

# 展示上传页面
def upload_page(request):
    return render(request,'home/upload.html')





# 执行上传
# # 接收数据 上传
# 上传图片 在数据库中存储的是 路径
# 图片本身放置于 磁盘中  比如说 /upload/pic
def upload_file(request):
    # 必须在页面中加入 {% csrf_token %} 
    # 才能完成请求
    # web网站 都有 csrftoken
    

    # 接收图片数据
    # 获取 FILES
    # print(request.FILES.get('files'))
    # print(type(request.FILES.get('files')))
    # 把数据 放入 files
    files = request.FILES.get('files')

    # 处理上传
    # 名字系统生成
    # 新名字 = 时间  + 后缀
    import time # 加载时间

    # 时间戳转化为date   小作业
    filename = str(time.time()) + "." + files.name.split('.').pop()

    print('新文件名字==========')
    print(filename)

    # 准备好 上传文件的目录
    # 与template 同级
    # static.pics
    directory = open("./static/pics/"+filename,"wb+")

    # 存文件 django 原理
    # 大型文件
    # 分块接收
    # 大事化小 小的一个一个接收
    
    # 分段写入
    # files.chunks() 代表的每一段
    for chunk in files.chunks():
        directory.write(chunk)
    directory.close()


        




    return HttpResponse('上传成功')
    


# 设置cookie 和session


# cookie
def setcookie(request):
    # set_cookie(key,values)
    res = HttpResponse('setcookie成功成功')
    res.set_cookie('key','123456')
    return res

def getcookie(request):
    # request.COOKIES.get('key')
    # 从请求中
    print(request.COOKIES.get('key'))

    return HttpResponse('get cookie成功')

# session
def setsession(request):
    # res = HttpResponse('setcookie成
    # 功成功')
    request.session['name'] = 'qiutianhao'

    return HttpResponse('session name成功')

def getsession(request):
    print(request.session.get('name'))

    return HttpResponse('get session ')