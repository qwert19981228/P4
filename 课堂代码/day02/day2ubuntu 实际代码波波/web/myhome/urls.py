from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    # url(r'^data/$', views.data,name='myhome_data'),
    url(r'^$', views.index),
    url(r'^addpage/$', views.addpage,name="myhome_addpage"),
    url(r'^add/$', views.addData,name="myhome_add"),
    url(r'^select/$', views.select,name="myhome_select"),
    url(r'^del/([0-9]+)/$', views.delData,name="myhome_del"),
]
