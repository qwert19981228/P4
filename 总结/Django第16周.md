# Django

## 虚拟环境

#### 安装虚拟环境

```
pip install virtualenv/virtualenvwrapper
```

#### 在指定位置创建虚拟环境文件夹

#### 启动虚拟环境

```
activate(在Scripts文件夹下)
```

#### 将activate加入环境变量



## Django

|   M    |    V     |    T     |
| :----: | :------: | :------: |
| model  |   view   | template |
| 数据层 | 业务逻辑 |   模版   |

#### 特点

1. 快速开发: Django的宗旨在于帮助开发人员快速从概念到完成应用程序
2. 安全可靠: Django认真对待安全性,帮助开发人员避免许多常见的安全错误
3. 超可伸缩性: Web上的一些最繁忙的网站利用了Django快速灵活扩展的能力

#### 安装Django

```
pip install Django
```

#### 创建项目

```
python startproject 项目名
```

#### 启动项目

```
python manage.py runserver
```

#### 创建应用

```
python manage.py startapp 应用名
```

#### 创建视图

```
from django.http import HttpResponse
# 定义视图函数，业务逻辑
def index(request):
    # 返回
    return HttpResponse('Hello World!!!')
```

#### 修改项目路由

```
from django.conf.urls import url,include       # 添加include
from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', include('myweb.urls')),          # 添加指定的路径
]
```

#### 创建应用路由

```
from django.conf.urls import url
from . import views                            # 导入视图

urlpatterns = [
    url(r'^hello/',views.index),
]
```

#### 使用模版

```
先创建template文件夹
html文件创建在template里
在项目settings里 TEMPLATES模块设置选项
'DIRS': [os.path.join(BASE_DIR,"templates")]

在应用路由中添加一个路由
url(r'^tmp$',views.tmp,name='myweb_tmp')

在视图中添加一个函数
def tmp(request):
    # 加载一个模块
    return render(request,'index.html')
```

####  参数路由

```
# 位置参数路由
将路由给则匹配到的内容当成参数传给视图函数 是有函数必须要有形参
(r'hello/([0-9]{2})',views.index)

# 关键字参数
(r'hello/(?P<形参名字>[0-9]{2})',views.index)

# 默认值参数 定义两个路由规则指向一个视图函数
(r'hello/$',views.index)
(r'hello/([0-9])/$',views.index)
```

#### 反向解析

```
给内部使用  
可以根据路由的name属性的值 动态获取url地址
在模板里面使用 {% url '路由的名' %}
在视图当中使用 
from django.core.urlresolvers import reverse
reverse('路由的名')
```



## 数据库操作

#### 配置model

1. 安装数据库

2. 创建数据库

3. 安装pymysql

   ```
   pip install pymysql
   ```

4. 修改配置文件

   ```
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'stu',  		# 数据库的名字
           'USER': 'root', 		# 链接数据库的账户
           'PASSWORD': '123456',  	# 数据哭的密码
           'HOST': '127.0.0.1',  	# 数据库的地址
           'PORT': '3306',        	# 数据库的端口号
   	}
   }
   
   把当前的应用导入
   INSTALLED_APPS = [
   	. . .
   	'myhome',
   ]
   ```

5. 导入pymysql

   ```
   在settings.py同级目录下的__init__.py导入pymysql
   import pymysql
   pymysql.install_as_MySQLdb()
   ```

#### 模型定义

1. 定义模型

   修改应用下的models.py

   在不指定表名的情况下 自动生成的表名  应用名_类名

   一个类就算是一个表,类里面的属性就是字段名

   如果不指定主键 会自动创建一个主键

   ```
   class User(Models.model):
   	name = models.CharField(max_length=50,null=True)
   ```

2. 生成迁移文件

   ```
    python manage.py makemigrations
   ```

3. 执行迁移

   ```
   python manage.py migrate
   ```

#### 增删改查

##### 实例化

```
from . import models
ob = models.User()# 得到数据库 user类
```

##### 添加数据

```
data = {xx:xx,xxx:xxx}
ob = models.User(**data)
ob.save()
```

##### 查询数据

```
obs = models.User.objects.all()   # 查所有
obs = models.User.objects.filter( . . . )  	# 条件 获取所有符合条件的数据
obs = models.User.objects.get(...)  		# 条件 执行单个条件 ,查到两条数据会报错
filter 和 all 都是迭代器    get 不是
```

##### 删除数据

```
obs.delete()   # 把obs中的结果全部删除
```

##### 更新数据

```
先查再改

obs.属性 = ' ' 
obs.save()
```

**如何把数据传给页面?**

使用render的第三个参数 该参数 须是字典形式



## 模型关系

### 一对一

> 两张表 一条数据对应一条数据

```
models中 创建副类 添加的字段
models.OneToOneField(主类,on_delete=models.CASCADE)
```

#### 添加数据

```
添加用户信息
u = models.User(name="zhansgan")
添加关联信息
w = models.Wife()
w.name='zhsnagnlp'
w.uid= u
```

#### 查询数据

```
通过老公差老婆
lg = models.User.objects.first()
print(lg.name)
print(lg.wife.wname)
通过老婆找老公
w = models.Wife.objects.first()
print(w.wname)
print(w.uid.name)
```

### 一对多

> 两个模型 一条数据对应多个信息

#### 添加数据

```
s = models.Stu()
s.sname='zhsna'
s.cid = 数据对象(models.Class.object.get(id=1))
```

#### 查询数据

```
根据学员差班级
s = models.Stu.objects.first()
s.cid.classname
根据班级查学员
c = models.Class.objects.first()
c.类名_set.all()
```

### 多对多

> manyTomany
>
> 两个模型但是会创建三个表,一个表只存关系

#### 添加关系

> 班级表 老师表  一个班级有多个老师 一个老师对应多个班级

```
给班级添加老师
t = models.Teacher.objects.get(id=)
c = models.Classs.objects.all()
t.cid.add(c[0],c[1])
```

#### 删除

只删除当前数据和当前数据对应的关系

#### 查询

```
根据班级查老师 
c = models.Classs.objects.get(id=)
print(c.teacher_set.all())

根据老师查班级
t = models.Teacher.objects.get(id=)
print(t.cid.all())
```



## 后台管理

自动管理界面是Django最强大部分之一

### 创建账户

创建一个管理员账户:项目创建好后台输入127.0.0.1:8000/admin/ 会出现登录界面

在m anage.py同级目录,命令行输入

```
python manage.py createsuperuser
```

需要添加用户名,邮箱和密码

### 添加模型

进入应用的admin.py文件,添加模型

```
from django.contrib import admin
from . import models
admin.site.register(models.User)
```

### 添加`__str__`

```
def __str__(self):
    return self.name(字段名)
```

### 修改admin

```
class UsersAdmin(admin.ModelAdmin):
    # 要展示的字段
    list_display = ('id','name','password','age','addtime')

    # 每一页显示多少条数据，默认是100条
    list_per_page = 5

    # 设置默认排序字段，负号表示降序排序
    ordering = ('id',)

    # 设置可编辑的字段
    list_editable = ['name','password','age']

    # 过滤器
    list_filter = ('name','age')

    # 搜索字段
    search_fields = ('name','age')
    # 时间分层筛选
    date_hierarchy = 'addtime'
admin.site.register(models.Users,UsersAdmin)
```

### 本地化

```
LANGUAGE_CODE = 'zh-Hans'   #  后台默认是英文 修改成中文

TIME_ZONE = 'Asia/Shanghai'     # 设置时区

USE_TZ = False  
```



## 重定向

### 利用js重定向

```
return HttpResponse('<script>location.href="'+path+'"</script>')
```

### 利用redirect

```
return redirect('reindex/')
return redirect(reverse('myhome_reindex'))
```



## request对象

path   返回路径  不包括域名

method   请求方式

GET  获取用户get方式提交的数据

​	request.GET['key']	如果用户没有提交数据会报错

​	request.GET.get('key')	如果用户没有提交数据 返回none 不会报错

​	request.GET.get('key',3)	如果用户没有提交数据 返回3

POST  获取用户POST方式提交的数据

FILES  文件上传

1. 添加路由

   返回表单页面   使用post提交一定要添加enctype

   接收用户提交的数据

2. 接收用户数据并写入到文件

   request.FILES

   写入数据

   在项目中创建static 目录

GET POST

一键一值

GET[ ]

GET.get( )

GET.dict( ) 返回字典

一键多值

GET.getlist('key')



## cookie 和 session

http 无状态 无法记录用户的行为 但是有时候需要记录用户的信息

### cookie 

将数据存储到本地(浏览器) 不安全

设置cookie  在响应对象设置

```
res = HttpResonse('设置cookie')
res.set_cookie('key','value')
return res
```

获取cookie  在请求对象获取

```
request.COOKIES.get('key')
```

### session

数据存储到服务端(数据库,文件,内存)

session会产生一个键 叫sessionid  将sessionid存到客户端

设置和获取都在request对象

```
def setsession(request):
    request.session['uname']='zhansagn'
    return HttpResponse('SHEHZISESSION')

def getsession(request):
    print(request.session.get('uname'))
    request.session.clear()   # 清空会话信息 不会删除会话
    request.session.flush()   # 删除会话
    return HttpResponse('获取session')
```



## 漏洞攻击

在django的模板中 默认会把变量中的 html,css,js等标签转义输出 
可以在输出变量时关闭自动转义 
{{ shtml|safe }}

为什么要把变量中的标签内容自动转义
涉及到web安全,xss攻击 
**XSS**是一种在web应用中的计算机安全漏洞，它允许恶意web用户将代码植入到提供给其它用户使用的页面中

**sql注入攻击**

 在你把用户提交的内容和你的sql语句做拼接时,会暴露

**解决方法**

1. 在进行数据库相关操作时,使用预处理方法, sql语句和参数进行分类,先执行sql语句,在给定参数
2. 不要相信用户提交的数据 过滤关键字及特殊符合
3. 使用框架中的模型进行数据库的操作



## 自定义标签,过滤器

在当前应用下 创建文件夹 (templatetags)并创建文件(根据你的项目情况进行命名)

#### 自定义过滤器

```
from django import template
register = template.Library()
# 自定义过滤器
@register.filter
def kong_upper(val):
    # print ('val from template:',val)
    return val.upper()
```

#### 自定义标签

```
from django.utils.html import format_html
@register.simple_tag
# 自定义标签
def jia(a,b):
    res = int(a) + int(b)
    return res
```

> 需要在末尾中导入文件[记得重启项目!要加载新文件]

```
{% load 文件名 %}
{{ 变量|kong_upper }}
{% jia 1 2 %}
```

