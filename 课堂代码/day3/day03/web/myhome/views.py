from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
# def index(request):
#     return render(request,'myhome/index.html')


# =======================================
# 一对一
def oto(request):
    # 添加用户
        # data = {'name':'yy','age':23,'email':'1361074646@163.com','password':'123456'}
        # ob = models.User(**data)
        # print(ob)
        # ob.save()
        # # 添加关联信息
        # ob1 = models.Wife()
        # ob1.wname='yylp'
        # ob1.uid=ob
        # ob1.save()
    # 查询数据
        # 通过 wife 查找user表的数据  # 老婆.外建.老公
        # w = models.Wife.objects.first()
        # print(w)
        # print(w.uid.name)
        # print(w.uid.age)
         # 通过 user 查找wife表的数据 # 老公.老婆的类名(小写).老婆的属性名
        # u = models.User.objects.get(id=11)
        # print(u.wife.wname)
    # 删除信息
        # w = models.Wife.objects.first()
        # w.delete()
        # u = models.User.objects.get(id=12)
        # u.delete()

    
    return HttpResponse('一对一')

# 一对多  
def ots(request):
    # 添加班级
        # ob = models.Class(classname="py11")
        # ob.save()
        # ob2 = models.Class(classname="py15")
        # ob2.save()
        # ob = models.Stu()
        # ob.sname='wbk'
        # 通过赋值关联属性 来做到关联
        # 类似 班级id = 数据库查询一个id 出来

        # ob.cid= models.Class.objects.get(id=1)
        # ob.save()
    # 数据查询
    # 根据学员查班级
    # s = models.Stu.objects.first()
    # print(s.sname)
    # print(s.cid.classname)
    # 根据班级查学员
    c = models.Class.objects.first()
    print(c)
    print(c.stu_set.all())
    
    return HttpResponse('一对多')

# 多对多  
def mtm(request):
    # 添加班级
    # c1 = models.Classs(classname='py15')
    # c1.save()
    # c2 = models.Classs(classname="py11")
    # c2.save()
    # c3 = models.Classs(classname="py16")
    # c3.save()

    # # 添加一个老师
    # t = models.Teacher(tname='卍w')
    # t.save()

    # 给老师添加班级
    # c = models.Classs.objects.all()
    # t = models.Teacher.objects.first()
    # t.cid.add(c[1],c[2])
    # t = models.Teacher(tname="sg")
    # t.save()
    # t.cid.add(c[0])

    # 根据老师查班级
    # t = models.Teacher.objects.first()
    # print(t.cid.all())
    # 根据班级找老师
    # c = models.Classs.objects.first()
    # print(c)
    # print(c.teacher_set.all())

    # 删除 删除班级 病删除对应关系
    # c = models.Classs.objects.first()
    # c.delete()

    # 给班级添加老师
    t = models.Teacher(tname="sg")
    t.save()
    c = models.Classs.objects.first()
    c.teacher_set.add(t)
    return HttpResponse('多对对')




# 总结
# 多你就使用all即可 哈哈哈哈
















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
    # obs = models.User.objects.filter(name__contains='i')
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
    data = request.POST.dict()
    data['age']=int(data['age'])
    data.pop('csrfmiddlewaretoken')
    print(data)
    ob = models.User(**data)
    ob.save()
    # return HttpResponse('数据添加成功')
    return HttpResponse(str(data))

def select(request):
    # 获取数据
    ob = models.User.objects.all()

    return render(request,'myhome/select.html',{'info':ob})

def delData(request,uid):
    # 删数据
    ob = models.User.objects.get(id=uid)
    ob.delete()
    return HttpResponse('删除成功')
    