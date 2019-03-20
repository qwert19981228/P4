# Django

## 虚拟环境

#### 安装虚拟环境

```
pip install virtualenv/virtualenvwrapper
```

#### 89在指定位置创建虚拟环境文件夹

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

### 特点

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