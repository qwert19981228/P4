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

def mtm(request):
	# 添加数据
	# 添加班级
	# class1 = models.Classes(classname='p1')
	# class2 = models.Classes(classname='p2')
	# class3 = models.Classes(classname='p3')
	# class1.save()
	# class2.save()
	# class3.save()
	# # 添加一个老师
	# t = models.Teacher(tname='波老师')
	# t.save()

	# 给老师添加班级
	# 先把 操作的老师 班级 查询出来
	t = models.Teacher.objects.get(id=3)
	c = models.Classes.objects.all()
	# 执行添加 外键在 teacher身上
	t.cid.add(c[1],c[2])  # 老师外键add参数给你要加的班级

	# 新老师添加班级
	# 加一个老师
	# t = models.Teacher(tname="苍老师")
	# # 外键在 teacher 身上
	# c = models.Classes.objects.all() # 班级
	# t.save()
	# # 给新老师添加班级
	# t.cid.add(c[0])

	# 根据班级查询老师
	# 班级外键 只能通过_set方法 去查找
	# c = models.Classes.objects.first()
	# print(c)
	# print(c.teacher_set.all())

	# 根据老师查询班级
	# 因为老师 有外键 cid
	# 所以 可以直接使用 外键+all方法
	# t = models.Teacher.objects.first()
	# print(t.cid.all())


	# 删除
	# 删除班级
	# c= models.Classes.objects.first()
	# c.delete()

	# 给班级添加老师
	# c = models.Classes.objects.first()
	# t = models.Teacher.objects.all()
	# # t = models.Teacher.objects.get(id=3)
	# c.teacher_set.add(t[0],t[1],t[2])
	return HttpResponse('多对多')
