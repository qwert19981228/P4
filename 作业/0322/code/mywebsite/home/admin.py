from django.contrib import admin
from . import models
# Register your models here.
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
admin.site.register(models.User,UsersAdmin)