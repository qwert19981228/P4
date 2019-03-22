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

    url(r'^$', views.index, name="home_index"),
    url(r'^reindex/$', views.reindex, name="home_reindex"),
    url(r'^urlpath/$', views.url_path, name="home_urlpath"),
    url(r'^upload_page/$', views.upload_page, name="home_upload_page"),
    url(r'^upload_file/$', views.upload_file, name="home_upload_file"),
    url(r'^setcookie/$', views.setcookie, name="home_setcookie"),
    url(r'^getcookie/$', views.getcookie, name="home_getcookie"),
    url(r'^setsession/$', views.setsession, name="home_setsession"),
    url(r'^getsession/$', views.getsession, name="home_getsession"),

]
