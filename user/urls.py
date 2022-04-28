# -*- encoding : utf-8 -*-
# @Project -> File     ：HPAS -> urls         
# @IDE      ：PyCharm
# @Author   ：Fenglchen
# @Date     ：2022/4/5 3:27 下午
# @Software : macos python3.8
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    # 用户登陆
    path('login/', views.user_login_view, name='user_login'),
    # 用户注册
    path('register/', views.user_register_view, name='user_register'),
    # 验证码生成
    path('captcha/', views.get_captcha_view, name='get_captcha'),
    # 登陆检测
    path('login/login_check/', views.user_login_check_view, name='user_login_check'),
    # 注册检测
    path('register/register_check/', views.user_register_check_view, name='user_register_check'),
    # 登出
    path('log_out/', views.log_out_view, name='user_log_out'),
    # 个人详情页
    path('detail/', views.user_detail_view, name='user_detail'),

]
