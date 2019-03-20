from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse
from . import models
import time
# Create your views here.

# def index(request):
# 	return render(request,'home/index.html')

def oto(request):
	# # 添加用户
	# data = {'name':'cz','age':21,'email':'123@qq.com','password':'123456'}
	# ob = models.User(**data)
	# ob.save()
	# # 添加关联信息
	# # wife
	# # 实例化 wife
	# ob1 = models.Wife()
	# ob1.wname = '范冰冰'
	# ob1.uid = ob  # ob就是上面的用户
	# ob1.save()

	# # 查询数据
	# # 通过老婆 查询用户
	# # 老婆.外键.用户 w.uid.属性
	# w = models.Wife.objects.first()
	# print(w)
	# print(w.uid.name)
	# print(w.uid.age)
	#
	# # 通过user 来查询老婆
	# # 用户.老婆(小写).属性
	# u = models.User.objects.get(id=11)
	# print(u.wife.wname)

	# 删除信息
	# u = models.User.objects.get(id=11)
	# u.delete()


	return HttpResponse('一对一')

def ots(request):
	# 添加班级
	# ob = models.Class(classname='py01')
	# ob1 = models.Class(classname='py02')
	# ob.save()
	# ob1.save()

	# 添加学生
	# ob = models.Stu()
	# ob.sname = '蕾丝边女神'
	# # 学生关联班级
	# # foreignkey cid
	# ob.cid = models.Class.objects.get(id=1)
	# ob.save()
	#

	# 数据查询
	# 根据学员 查询班级
	# 多类对象.多类外键.一类属性名字
	s = models.Stu.objects.first()
	print(s.sname)
	# 返回的是对象 但是我们models中设置 返回直接返回name
	print(s.cid)
	print(s.cid.classname)
	print('---------------------------------')
	# 根据班级查询学员
	c = models.Class.objects.first()
	print(c)
	print(c.stu_set.all())
	return HttpResponse('一对多')
