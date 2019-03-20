from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse
from .models import User
import time
# Create your views here.

def index(request):
	return render(request,'home/index.html')

def dataAdd(request):
# 	# 数据的添加
# 	ob = User()
# 	ob.name = '小娜'
# 	ob.age = 18
# 	ob.email = '123@qq.com'
# 	ob.password = '123456'
# 	ob.save()
	return HttpResponse('数据的增删改查')

# 展示表单页面
def addpage(request):
	return render(request,'home/add.html')

# 执行添加的表单请求
def add(request):
	# 接收get参数 request.GET.dict()
	data = request.GET.dict()
	data['age'] = int(data['age'])
	print(data)
	ob = User(**data)
	ob.save()
	path = reverse('home_addpage')
	return HttpResponse('<script>location.href="'+path+'"</script>')

# 展示学生列表(重点)
# 把数据交给页面 使用render方法 第三个参数
def userlist(request):
	# 查询所有
	ob = User.objects.all()
	print(ob)

	return render(request,'home/list.html',{'info':ob})

# 删除操作
def delUser(request,uid):
	# 查询 uid 这条数据
	ob = User.objects.get(id=uid)
	# 执行删除
	ob.delete()
	path = reverse('home_userlist')
	return HttpResponse('<script>location.href="'+path+'"</script>')

# 展示修改页面
def updatepage(request,uid):
	ob = User.objects.filter(id=uid)
	return render(request,'home/update.html',{'info':ob})

def update(request):
	data = request.GET.dict()

	ob = User(**data)
	ob.name = data['name']
	ob.age = data['age']
	ob.email = data['email']
	ob.password = data['password']
	ob.save()
	path = reverse('home_userlist')

	return HttpResponse('<script>location.href="'+path+'"</script>')