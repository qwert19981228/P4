from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.


# 视图是以函数为载体的.
def index(request):
    return HttpResponse('hello') # 通过http去响应 响应信息 就是 hello


def abc(request):
    return HttpResponse('efg') # 通过http去响应 响应信息 就是 hello


#响应页面
def page(request):
    return render(request,'index.html')  # 会直接找 定义好的 模板位置 + 路径名


#位置参数  需要你定义个  变量 收一下哎 
#这里变量名字 不做限制
def title(request,year):
    return HttpResponse('参数我收到啦'+year)

#关键字传参
##这里变量名字 有限制
#跟url定义的 关键字对上
# def guan_title(request,month): 这里会报错 提示 没有year这个坑位
def guan_title(request,year):
    return HttpResponse('关键字参数我收到啦'+year)


#默认值传参
def detail(request,year='2020'):
    return HttpResponse('我是默认参数的处理'+year)


# 反向解析  reverse('url名字')
def turnover(request):
    print(reverse('over'))   # 会直接打印在 控制台(cmder)
    print(reverse('fall'))   # 会直接打印在 控制台(cmder)
    # path = reverse('over')  # 如果自己 跳自己  那就 爱的魔力转圈圈
    path = reverse('fall')
    return HttpResponse('<script>location.href="'+path+'"</script>')


def fall(request):
    return HttpResponse('我坠入爱河了')
