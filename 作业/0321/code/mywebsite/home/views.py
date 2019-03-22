from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse
from . import models
import time
# Create your views here.

def index(request):
	path = reverse('home_reindex')
	return redirect(path)

def reindex(request):
	return HttpResponse('我是重定向')


def url_path(request):
	# print(request)
	# print(request.path)
	# print(request.method)

	print(request.GET)
	print(request.GET['id'])
	print(request.GET.dict())
	print(request.GET.getlist('id'))
	print(request.GET.get('id'))

	return HttpResponse('臣妾做不到')

# 展示上传页面
def upload_page(request):
	return render(request,'home/upload.html')

# 执行上传
# 接收数据 上传
# 上传图片在数据库中存储的是路径
# 图片本身放置于磁盘中
def upload_file(request):
	# 必须在页面中加入{% csrf_token %}
	# 才能完成请求
	# web网站 都有 csrftoken

	# 接收图片数据
	# 获取FILES
	# 把数据放入files
	files = request.FILES.get('files')

	# 处理上传
	# 名字系统生成
	# 新名字 = 时间 + 后缀
	import time # 加载时间

	# 时间戳转化为date

	filename = str(time.strftime('%Y%m%d%H%M%S', time.localtime())) + "." + files.name.split('.').pop()

	print('新文件名字==========')
	print(filename)

	# 准备好 上传的文件夹
	# 与template 同级
	# static/pics
	directory = open("./static/pics/"+filename,'wb+')

	# 存文件 django 原理
	# 大型文件
	# 分块接收
	# 大事化小 小的一个一个接收

	# 分段写入
	# files().chunks() 代表的每一段
	for chunk in files.chunks():
		directory.write(chunk)
	directory.close()

	return HttpResponse('上传成功,小哥哥')

# 设置cookie 和 session
# cookie
def setcookie(request):
	res =HttpResponse('setcookie成功')
	res.set_cookie('key','123456')
	return res


def getcookie(request):
	# 从请求中
	print(request.COOKIES.get('key'))

	return HttpResponse('get cookie成功')

# session

def setsession(request):
	request.session['name'] = 'mxy是坏蛋'

	return HttpResponse('session name成功')


def getsession(request):
	# 从请求中
	print(request.session.get('name'))

	return HttpResponse('get session成功')
