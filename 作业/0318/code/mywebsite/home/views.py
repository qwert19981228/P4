from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
	return HttpResponse('hello')

def page(request):
	return render(request,'index.html')

def title(request,year):
	return HttpResponse('参数我收到了'+year)
def guan_title(request,year):
	return HttpResponse('关键字参数我收到了'+year)
def detail(request,year="2019"):
	return HttpResponse('我是默认参数的处理'+year)

# 反向解析 reverse('url名字')
def turnover(request):
	print(reverse('over'))
	print(reverse('fall'))
	path = reverse('fall')
	return HttpResponse('<script>location.href="'+path+'"</script>')

def fall(request):
	return HttpResponse('我坠入爱河了')