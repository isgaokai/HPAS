from django.contrib import admin

# Register your models here.
from user import models


# 定制admin管理站点显示模型
@admin.register(models.NormalUser)
class NormalUserAdmin(admin.ModelAdmin):
    # 需要显示的字段
    list_display = ('id', 'nickname', 'phone', 'email', 'password', 'last_login','is_deleted')
    # 设置哪些字段可以点击进入编辑界面 默认是第一个字段
    list_display_links = ('id', 'phone', 'email')

# 定制admin管理站点显示模型
@admin.register(models.Administrator)
class MyAdmin(admin.ModelAdmin):
    # 需要显示的字段
    list_display = ('id', 'nickname', 'phone', 'email', 'password', 'last_login','is_deleted')
    # 设置哪些字段可以点击进入编辑界面 默认是第一个字段
    list_display_links = ('id', 'phone', 'email')
