from django.conf.urls import url
# 加载 views 模块
from . import views

urlpatterns = [


    url(r'^$',views.index,name="admin_index"),
    url(r'^user/add/$',views.useradd,name="myadmin_user_add"),
    url(r'^user/userlist/$',views.userlist,name="myadmin_user_list"),

]
