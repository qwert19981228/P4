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
from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^data/$', views.dataAdd, name='home_dataAdd'),
    # 添加页面展示
    url(r'^addpage/$',views.addpage,name='home_addpage'),
    # 执行添加操作
    url(r'^add/$',views.add,name='home_add'),
    # 展示学生列表
    url(r'^userlist/$',views.userlist,name='home_userlist'),
    # 删除的路由 带上一个id
    url(r'^del/([0-9]+)/$', views.delUser, name='home_del'),
    # 修改
    url(r'^updatepage/([0-9]+)/$', views.updatepage, name='home_updatepage'),
    #
    url(r'^update/$', views.update, name='home_update'),

]
