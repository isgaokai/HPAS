import json
import re
from decimal import Decimal

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Tools.Tools import Tools
from myLog.models import Log
from user.models import NormalUser, Code, Administrator


# ajax检查验证码
def ajax_check_captcha_view(request):
    # 用户输入验证码
    input_captcha = request.GET.get('input_captcha', 'isnull')
    # session 中正确的验证码
    true_captcha = request.session.get('true_captcha', 'None')
    print(input_captcha, true_captcha)
    # 判断用户输入验证码是否和session中的一致
    if input_captcha.lower() != true_captcha.lower():
        # 输入错误
        return HttpResponse('false')
    else:
        # 输入正确
        return HttpResponse('true')


# ajax 检查用户名
def ajax_check_username_view(request):
    # 邮箱正则
    ePattern = re.compile(r'^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$')
    # 手机号正则
    mPattern = re.compile(r'^((13[0-9])|(19[8])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$')

    # 用户输入用户名
    input_username = request.GET.get('input_username')
    # 正则检验 手机号和邮箱均未通过
    if not ePattern.search(input_username) and not mPattern.search(input_username):
        # 正则检验未通过
        return HttpResponse('checkfalse')
    # 通过邮箱检验
    elif ePattern.search(input_username):
        # 数据库中查找该用户是否被注册
        if NormalUser.objects.filter(email=input_username).count() != 0:
            # 输入错误
            return HttpResponse('false')
        else:
            # 输入正确
            return HttpResponse('true')
    # 通过手机号检验
    else:
        # 数据库中查找该用户是否被注册
        if NormalUser.objects.filter(phone=input_username).count() != 0:
            # 输入错误
            return HttpResponse('false')
        else:
            # 输入正确
            return HttpResponse('true')


# ajax 检查用户密码
def ajax_check_password_view(request):
    # 用户输入密码
    input_password = request.GET.get('input_password')
    # 用户密码等级
    level = Tools.checkout_password(input_password)
    # 输入密码未通过检验
    if not level:
        return HttpResponse('False')
    # 低强度密码
    if level == 'LowSecurity':
        return HttpResponse('LowSecurity')
    # 中等强度密码
    elif level == 'MediumSecurity':
        return HttpResponse('MediumSecurity')
    # 高强度密码
    elif level == 'HighSecurity':
        return HttpResponse('HighSecurity')
    # 极高强度密码
    else:
        return HttpResponse('ExtermeHighSecurity')


# ajax 检查激活码
def ajax_check_code_view(request):
    # 用户输入激活码
    input_code = request.GET.get('input_code')
    # 输入激活码未通过验证
    if not input_code or len(input_code) != 12:
        return HttpResponse('false')

    # 数据库中查找该激活码是否有效
    if Code.objects.filter(cdk=input_code, state=1).count() != 0:
        # 激活码可用
        return HttpResponse('true')
    else:
        # 激活码不可用
        return HttpResponse('false')


# ajax 检查admin用户名
def ajax_check_admin_username_view(request):
    # 邮箱正则
    ePattern = re.compile(r'^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$')
    # 手机号正则
    mPattern = re.compile(r'^((13[0-9])|(19[8])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$')

    # 用户输入用户名
    input_username = request.GET.get('input_username')

    # 正则检验 手机号和邮箱均未通过
    if not ePattern.search(input_username) and not mPattern.search(input_username):
        # 正则检验未通过
        return HttpResponse('checkfalse')
    # 通过邮箱检验
    elif ePattern.search(input_username):
        # 数据库中查找该用户是否被注册
        if Administrator.objects.filter(email=input_username).count() != 0:
            # 输入错误
            return HttpResponse('false')
        else:
            # 输入正确
            return HttpResponse('true')
    # 通过手机号检验
    else:
        # 数据库中查找该用户是否被注册
        if Administrator.objects.filter(phone=input_username).count() != 0:
            # 输入错误
            return HttpResponse('false')
        else:
            # 输入正确
            return HttpResponse('true')


# ajax检查昵称是否存在
def ajax_check_nickname_view(request):
    # 用户输入昵称
    input_nickname = request.GET.get('input_nickname')
    # 检查是否存在
    if NormalUser.objects.filter(nickname=input_nickname).count() != 0:
        # 输入错误
        return HttpResponse('false')
    else:
        # 输入正确
        return HttpResponse('true')


# ajax加载数据
def ajax_load_data_view(request):
    try:
        # 获取已经加载页面
        page_count = request.GET.get('page_count', '-1')
        # 转换类型
        page_count = int(page_count)
    except:
        return HttpResponse('false')
    # 判断是否有效以及在范围内
    if page_count == -1:
        return HttpResponse('false')
    # 目标页面+1
    page_count += 1

    # 最终返回结果
    result = []

    # 查找全部用户
    users = NormalUser.objects.all().order_by('id')
    # 声明分页器对象
    user_category_paginator = Paginator(object_list=users, per_page=16)

    try:
        # 获取当前页面的用户
        goal_page = user_category_paginator.page(page_count).object_list
    except:
        return HttpResponse('false')

    # 添加至返回结果
    for user in goal_page:
        result.append({'user_id': user.id, 'user_nickname': str(user.nickname), 'user_phone': str(user.phone),
                       'user_email': str(user.email),
                       'user_last_login': str(user.last_login), 'user_used_code': str(user.used_code),
                       'user_is_deleted': user.is_deleted})
    # 转换为json格式
    result = json.dumps(result)
    return HttpResponse(result)

# ajax搜索用户
def ajax_search_user_view(request):
    # 获取输入用户名字
    input_search_user = request.GET.get('input_search_user')

    # 检测用户是否登陆
    now_user, username_head, username_tail = Tools.check_user_login(request)
    if now_user:
        # 添加日志
        log_content = now_user + '管理员搜索了用户昵称:' + str(input_search_user)
        Log.objects.create(log_content=log_content)

    # 查询是否存在该用户
    goal_user= NormalUser.objects.filter(nickname=input_search_user)
    # 查找失败
    if not goal_user:
        return HttpResponse('false')
    # 查找成功
    goal_user = goal_user[0]
    result = goal_user.id


    return HttpResponse(result)

# ajax删除用户
def ajax_delete_user_view(request):
    # 获取被删除用户的id
    delete_user_id = request.GET.get('delete_user_id')

    # 检测用户是否登陆
    now_user, username_head, username_tail = Tools.check_user_login(request)
    if now_user:
        # 添加日志
        log_content = now_user + '管理员删除了用户ID:' + str(delete_user_id)
        Log.objects.create(log_content=log_content)

    # 查询是否存在该用户
    goal_user = NormalUser.objects.filter(id=delete_user_id,is_deleted=False)
    # 查找失败
    if not goal_user:
        return HttpResponse('false')
    # 查找成功
    goal_user = goal_user[0]
    goal_user.is_deleted = True
    goal_user.save()

    return HttpResponse('true')

# ajax修改用户密码
def ajax_change_user_password_view(request):
    # 获取被修改用户的id
    change_user_id = request.GET.get('change_user_id')
    # 修改后的密码
    new_password = request.GET.get('new_password')
    print(change_user_id,new_password)

    # 检测用户是否登陆
    now_user, username_head, username_tail = Tools.check_user_login(request)
    if now_user:
        # 添加日志
        log_content = now_user + '管理员修改了用户ID:' + str(change_user_id) +'密码'
        Log.objects.create(log_content=log_content)

    # 查询是否存在该用户
    goal_user = NormalUser.objects.filter(id=change_user_id,is_deleted=False)
    # 查找失败
    if not goal_user:
        return HttpResponse('false')
    # 查找成功
    goal_user = goal_user[0]
    password_salt, password = Tools.password_encryption(new_password,goal_user.password_salt)
    goal_user.password = password
    goal_user.save()

    return HttpResponse('true')