课程目标:

课件中的1 2 3 讲完

学习目的:
django

安装
创建应用

url
视图
数据render

这些简单的

----------------



MVC   降低耦合性
		M     model         数据层  =====  数据
		V     view          模板    =====  HTML css
		C     controller    控制器  =====  业务逻辑  处理用户的请求和响应

MVT 
	M   model      数据层
	V   view       业务逻辑
	T   template   模板

路由:
	指路的人  接收用户请求(url)  分发指定的函数处理请求

安装:
    请先根据课件安装虚拟环境(包含了linux 与 windows安装)
	pip install  django==1.11.*

	sudo pip3 install django==1.11.*
卸载包
	pip uninstall 包名

pip 包管理工具
	快速下载三方模块
	解决依赖

1.使用djang创建一个项目
	django-admin startproject 项目的名字

2.启动项目
	在manage.py的同级目录下 
	python manage.py runserver

3.创建一个应用  用户输入127.0.0.1:8000/hello 返回一个字符串
		1.创建应用 在manage.py同级目录下执行
			python manage.py startapp 应用名

			mysite/
			├── manage.py
			├── mysite
			│   ├── __init__.py
			│   ├── settings.py
			│   ├── urls.py
			│   └── wsgi.py
			└── myweb
			    ├── admin.py
			    ├── apps.py
			    ├── __init__.py
			    ├── migrations
			    │   └── __init__.py
			    ├── models.py
			    ├── tests.py
			    └── views.py

		2.找到home下views 添加视图函数(建立一个home应用)
			# 不要忘记 一i纳入HttpResponse
			from django.http import HttpResponse
			# Create your views here.
			def index(request):
				return HttpResponse('hello')

		3.找到项目同名目录下的urls 添加路由(记得include)
			from django.conf.urls import url,include
			from django.contrib import admin

			urlpatterns = [
			    url(r'^admin/', admin.site.urls),
			    url(r'^', include('home.urls'))
			]
		4.在home目录下创建子路由 urls

			from django.conf.urls import url
			from . import views
			urlpatterns = [
			    url(r'^hello/', views.index),
			    url(r'^abc/', views.abc)
			]

	用户输入网址   由跟路由匹配 分发到子路由
	子路由接收到请求 进行匹配 分发给指定视图函数来处理响应
	自动执行指定的视图函数

响应一个模板
	1.在manage.py同级目录下创建一个文件夹 template
	2.修改配置文件  settings.py
		TEMPLATES = [
		    {
		        'BACKEND': 'django.template.backends.django.DjangoTemplates',
		        # 这是 os.path.join()函数用于路径拼接文件路径。 意思是根目录下的tpl
		        'DIRS': [os.path.join(BASE_DIR,'template')],
		        'APP_DIRS': True,
		        'OPTIONS': {
		            'context_processors': [
		                'django.template.context_processors.debug',
		                'django.template.context_processors.request',
		                'django.contrib.auth.context_processors.auth',
		                'django.contrib.messages.context_processors.messages',
		            ],
		        },
		    },
		]
	3.根据请求响应页面
		home/views
			def page(request):
				return render(request,'文件路径')

	4.在template 目录下创建html

路由:
	位置参数路由  
    将路由给则匹配到的内容当成参数传给视图函数 是有函数必须要有形参
	(r'hello/([0-9]{2})',views.index)
	127.0.0.1:8000/hello?id=1


	关键字参数
	(r'hello/(?P<形参名字>[0-9]{2})',views.index)


	默认值参数 定义两个路由规则指向一个视图函数
	(r'hello/$',views.index)
	(r'hello/([0-9])/$',views.index)
	def index(request,p='1'):

	反向解析: (给内部使用)
    可以根据路由的name属性的值 动态获取url地址
		在模板里面使用 {% url '路由的名' %}
		在视图当中使用 
			from django.core.urlresolvers import reverse
			reverse('路由的名')



404讲解
直接看课件吧 顺手改


写一个模板中传递数据的例子



------------------
奇葩问题:
from . import views 为什么在外面的urls 无法引用?
因为你外部没有views文件啊!
注意路径

奇葩问题:
你从windows复制代码进入虚拟机 
记得 缩进错误
可能会出错

taberror 这就是缩进错误  你根据pycharm 提示 你重新缩进即可
