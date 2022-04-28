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
    # ajax检查admin用户名是否存在
    path('check_admin_username/',views.ajax_check_admin_username_view, name='check_admin_username'),
    # ajax检查用户昵称是否存在
    path('check_nickname/',views.ajax_check_nickname_view, name='check_nickname'),
    # ajax加载数据
    path('load_data/', views.ajax_load_data_view, name='load_data'),
    # ajax搜索用户
    path('search_user/',views.ajax_search_user_view,name='search_user'),
    # ajax删除用户
    path('delete_user/', views.ajax_delete_user_view, name='delete_user'),
    # ajax修改用户密码
    path('change_user_password/',views.ajax_change_user_password_view, name='change_user_password'),
    # ajax检验用户旧密码
    path('check_old_password/', views.ajax_check_old_password_view, name='check_old_password'),
]
