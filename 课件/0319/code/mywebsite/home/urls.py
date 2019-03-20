"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# 加载 views 模块
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^data/$', views.dataAdd,name='home_dataAdd'),
    # 添加页面展示
    url(r'^addpage/$', views.addpage,name='home_addpage'),
    
    # 执行添加操作
    url(r'^add/$', views.add,name='home_add'),
    # 展示学生列表
    url(r'^userlist/$', views.userlist,name='home_userlist'),
    # 删除的路由 带上一个id
    url(r'^del/([0-9]+)/$', views.delUser,name='home_del'),

    
    
    # url(r'^hello/', views.index),
    # url(r'^abc/', views.abc),
    # url(r'^page/', views.page),
    # url(r'^title/([0-9]{4})/$', views.title,name='title'), # 位置参数
    # url(r'^guan_title/(?P<year>[0-9]{4})/$', views.guan_title), # 关键字参数

    # # 默认值参数
    # # 定义2条路由
    # # url(r'^detail/', views.detail), # 不传参数的url  这里呢因为没有$ 所以匹配会把下面的的 盖住. $表示匹配结束
    # url(r'^detail/$', views.detail), # 不传参数的url
    # url(r'^detail/([0-9]{4})/$', views.detail), # 传参数

    # # 反向解析
    # url(r'^turnover/$', views.turnover,name='over'), 
    # url(r'^fall/$', views.fall,name='fall'), 

    
    
    
]
