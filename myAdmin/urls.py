# coding:utf-8
# @Project -> File     ：HPAS -> urls         
# @IDE      ：PyCharm
# @Author   ：Fenglchen
# @Date     ：2022/4/25 09:38
# @Software : macos python3.8
from django.urls import re_path, path

from myAdmin import views

app_name = 'myadmin'

urlpatterns = [
    # 用户管理主页面
    path('home/',views.myAdmin_main_view,name='admin_home'),
    # 管理员登陆页面
    path('login/', views.myAdmin_login_view, name='admin_login'),
    # 管理员登陆检测
    path('login/login_check/', views.myAdmin_login_check_view, name='admin_login_check'),
    # 登出
    path('log_out/', views.log_out_view, name='admin_log_out'),
    # 新增用户页面
    path('adduser/',views.myAdmin_adduser_view, name='admin_adduser'),
    # 新增用户验证视图
    path('adduser/check/',views.myAdmin_adduser_check_view, name='admin_adduser_check'),
    # 用户管理详情页面
    path('user_detail/',views.myAdmin_user_detail_view, name='admin_user_detail')
]