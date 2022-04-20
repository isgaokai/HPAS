# -*- encoding : utf-8 -*-
# @Author : Fenglchen
from django.urls import path

from ajax import views

app_name = 'ajax'

urlpatterns = [
    # ajax检查验证码正确与否
    path('check_captcha/', views.ajax_check_captcha_view, name='check_captcha'),
    # ajax检查用户名是否存在
    path('check_username/', views.ajax_check_username_view, name='check_username'),
    # ajax检查密码正确以及强度
    path('check_password/', views.ajax_check_password_view, name='check_password'),
    # ajax检查激活码
    path('check_code/', views.ajax_check_code_view, name='check_code'),
]
