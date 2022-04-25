import re
from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Tools.Tools import Tools
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

    print(input_code)
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
    input_nickname= request.GET.get('input_nickname')
    # 检查是否存在
    if NormalUser.objects.filter(nickname=input_nickname).count() != 0:
        # 输入错误
        return HttpResponse('false')
    else:
        # 输入正确
        return HttpResponse('true')