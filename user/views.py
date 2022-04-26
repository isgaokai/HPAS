from django.shortcuts import render

# Create your views here.
import random
import re
import string
import time
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Tools.Tools import Tools

# Create your views here.
from myLog.models import Log
from user.captcha.image import ImageCaptcha

from user.models import NormalUser, Code, Administrator


# 用户登陆视图
def user_login_view(request):
    # 邮箱正则
    ePattern = re.compile(r'^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$')
    # 手机号正则
    mPattern = re.compile(r'^((13[0-9])|(19[8])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$')

    # 获取cookie中的username
    cookie_username = request.COOKIES.get('username')
    # 获取cookie中的password
    cookie_password = request.COOKIES.get('password')
    print(cookie_username,cookie_password)
    # cookie 中未存在
    if not cookie_username or not cookie_password:
        return render(request, 'normalUser_login.html')
    # 用户名未通过正则校验
    elif not ePattern.search(cookie_username) and not mPattern.search(cookie_username):
        return render(request, 'normalUser_login.html')

    # 手机号登陆
    if mPattern.search(cookie_username) and cookie_password:
        # 验证数据库内是否存在该用户
        if NormalUser.objects.filter(phone=cookie_username,password=cookie_password,is_deleted=False).count() != 0:
            # session添加登陆状态为'yes'
            request.session['logged_in'] = 'yes'
            # session添加用户名
            request.session['username'] = cookie_username
            # session添加用户类型
            request.session['user_type'] = 'normalUser'
            # 添加日志
            log_content = cookie_username + '访问了网站'
            Log.objects.create(log_content=log_content)
            # 返回响应
            return redirect('/home/')
        else:
            return render(request, 'normalUser_login.html')
    # 邮箱登陆
    elif ePattern.search(cookie_username) and cookie_password:
        # 验证数据库内是否存在该用户
        if NormalUser.objects.filter(email=cookie_username, password=cookie_password,is_deleted=False).count() != 0:
            # session添加登陆状态为'yes'
            request.session['logged_in'] = 'yes'
            # session添加用户名
            request.session['username'] = cookie_username
            # session添加用户类型
            request.session['user_type'] = 'normalUser'
            # 添加日志
            log_content = cookie_username + '访问了网站'
            Log.objects.create(log_content=log_content)
            # 返回响应
            return redirect('/home/')
        else:
            return render(request, 'normalUser_login.html')
    else:
        return render(request, 'normalUser_login.html')


# 用户登陆验证视图
def user_login_check_view(request):
    # 邮箱正则
    ePattern = re.compile(r'^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$')
    # 手机号正则
    mPattern = re.compile(r'^((13[0-9])|(19[8])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$')
    # 密码正则
    pPattern = re.compile(
        r'^[a-zA-Z0-9]\w{6,16/^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])|(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])|(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])).{6,}|(?:(?=.*[A-Z])(?=.*[a-z])|(?=.*[A-Z])(?=.*[0-9])|(?=.*[A-Z])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*[0-9])|(?=.*[a-z])(?=.*[^A-Za-z0-9])|(?=.*[0-9])(?=.*[^A-Za-z0-9])|).{6,16}$')

    try:
        # 接收用户输入用户名
        username = request.POST.get('txt_username')
        # 接收用户输入密码
        password = request.POST.get('txt_password')
        # 接收用户输入验证码
        captcha = request.POST.get('txt_captcha').lower()
        # 获取session中的正确验证码
        true_captcha = request.session.get('true_captcha').lower()
        # 接收用户是否选择七天免登陆
        autologin = request.POST.get('autologin')
    except:
        return redirect('/home/')
    print(username,password,captcha,true_captcha,autologin)

    # 正则及其他检验
    if not ePattern.search(username) and not mPattern.search(username):
        return redirect('/user/login/')
    elif not pPattern.search(password) or Tools.checkout_password(password) == 'LowSecurity' or captcha != true_captcha:
        return redirect('/user/login/')

    # 通过手机号登陆
    if mPattern.search(username):
        # 查询当前库内是否存在该用户
        if NormalUser.objects.filter(phone=username,is_deleted=False).count() != 0:
            # 定位用户
            user = NormalUser.objects.filter(phone=username)[0]
            # 对用户输入的密码与库内盐进行比对 检验密码是否正确
            password_salt, password = Tools.password_encryption(password, pwd_salt=user.password_salt)
            # 密码正确
            if password == user.password:
                # 返回响应
                result = redirect('/home/')
                # 对用户对最后登陆时间进行修改
                user.last_login = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 获取访问ip地址
                if request.META.get('HTTP_X_FORWARDED_FOR'):
                    ip = request.META.get("HTTP_X_FORWARDED_FOR")
                else:
                    ip = request.META.get("REMOTE_ADDR")
                # 对用户最后登陆ip进行修改
                user.last_ip = ip
                print('最后登陆ip{}'.format(ip))
                # 修改后需要保存
                user.save()
                # 判断用户是否选择七天免登陆
                if autologin:
                    # cookie添加用户名 时效7天
                    result.set_cookie('username', username, max_age=3600 * 24 * 7)
                    # cookie添加密码 时效7天
                    result.set_cookie('password', password, max_age=3600 * 24 * 7)
                # session添加登陆状态为'yes'
                request.session['logged_in'] = 'yes'
                # session添加用户名
                request.session['username'] = username
                # session添加用户类型
                request.session['user_type'] = 'normalUser'
                # 添加日志
                log_content = username + '访问了网站'
                Log.objects.create(log_content=log_content)
                # 返回
                return result
            else:
                return redirect('/user/login/')
        else:
            return redirect('/user/login/')
    # 通过email登陆
    else:
        # 查询当前库内是否存在该用户
        if NormalUser.objects.filter(email=username,is_deleted=False).count() != 0:
            # 定位用户
            user = NormalUser.objects.filter(email=username)[0]
            # 对用户输入的密码与库内盐进行比对 检验密码是否正确
            password_salt, password = Tools.password_encryption(password, pwd_salt=user.password_salt)
            # 密码正确
            if password == user.password:
                # 返回响应
                result = redirect('/home/')
                # 对用户的最后登陆时间进行修改
                user = NormalUser.objects.filter(email=username)[0]
                user.last_login = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 获取访问ip地址
                if request.META.get('HTTP_X_FORWARDED_FOR'):
                    ip = request.META.get("HTTP_X_FORWARDED_FOR")
                else:
                    ip = request.META.get("REMOTE_ADDR")
                # 对用户最后登陆ip进行修改
                user.last_ip = ip
                # 修改后需要保存
                user.save()
                # 判断用户是否选择七天免登陆
                if autologin:
                    # cookie添加用户名 时效7天
                    result.set_cookie('username', username, max_age=3600 * 24 * 7)
                    # cookie添加密码 时效7天
                    result.set_cookie('password', password, max_age=3600 * 24 * 7)
                # session添加登陆状态为'yes'
                request.session['logged_in'] = 'yes'
                # session添加用户名
                request.session['username'] = username
                # session添加用户类型
                request.session['user_type'] = 'normalUser'
                # 添加日志
                log_content = username + '访问了网站'
                Log.objects.create(log_content=log_content)
                # 返回
                return result
            else:
                return redirect('/user/login/')
        else:
            return redirect('/user/login/')


# 用户注册视图
def user_register_view(request):
    return render(request, 'normalUser_register.html')


# 用户注册验证视图
def user_register_check_view(request):
    # 密码正则
    pPattern = re.compile(
        r'^[a-zA-Z0-9]\w{6,16/^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])|(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])|(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])).{6,}|(?:(?=.*[A-Z])(?=.*[a-z])|(?=.*[A-Z])(?=.*[0-9])|(?=.*[A-Z])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*[0-9])|(?=.*[a-z])(?=.*[^A-Za-z0-9])|(?=.*[0-9])(?=.*[^A-Za-z0-9])|).{6,16}$')
    # 邮箱正则
    ePattern = re.compile(r'^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$')
    # 手机号正则
    mPattern = re.compile(r'^((13[0-9])|(19[8])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$')

    try:
        # 接收用户输入用户名
        username = request.POST.get('txt_username')
        # 接收用户输入密码
        password = request.POST.get('txt_password')
        # 接收用户输入的第二次密码
        re_password = request.POST.get('txt_re_password')
        # 接收用户输入激活码
        code = request.POST.get('txt_code')
        # 接收用户输入验证码
        captcha = request.POST.get('txt_captcha').lower()
        # 获取session中的正确验证码
        true_captcha = request.session.get('true_captcha').lower()
    except:
        return redirect('/home/')
    print(username,password,re_password,true_captcha,code,captcha)
    # 正则及其他检验
    if not ePattern.search(username) and not mPattern.search(username):
        return HttpResponse('/user/register/')
    elif not pPattern.search(password) or password != re_password or Tools.checkout_password(
            password) == 'LowSecurity' or captcha != true_captcha or len(code)!= 12:
        return HttpResponse('/user/register/')

    # 数据库中查找该激活码是否有效
    if Code.objects.filter(cdk=code,state=1).count() == 0:
        # 激活码不可用
        return HttpResponse('/user/register/')

    # 通过手机号注册
    if mPattern.search(username):
        if NormalUser.objects.filter(phone=username).count() == 0:
            # 事务控制
            try:
                with transaction.atomic():
                    # 返回响应
                    result = redirect('/user/login/')
                    # 获取访问ip地址
                    if request.META.get('HTTP_X_FORWARDED_FOR'):
                        ip = request.META.get("HTTP_X_FORWARDED_FOR")
                    else:
                        ip = request.META.get("REMOTE_ADDR")
                    # 对密码进行加盐
                    password_salt, password = Tools.password_encryption(password)
                    # 修改code 状态
                    goal_code = Code.objects.filter(cdk=code,state=1)[0]
                    goal_code.state = 0
                    goal_code.save()
                    # 创建对象
                    NormalUser.objects.create(phone=username, password=password, password_salt=password_salt,registered_ip_address=ip,used_code=code)
                    # 添加日志
                    log_content = username + '进行了注册'
                    Log.objects.create(log_content=log_content)
            except:
                return redirect('/user/register/')

            return result

        else:
            return redirect('/user/register/')
    # 通过email注册
    else:
        if NormalUser.objects.filter(email=username).count() == 0:
            # 事务控制
            try:
                with transaction.atomic():
                    # 返回响应
                    result = redirect('/user/login/')
                    # 获取访问ip地址
                    if request.META.get('HTTP_X_FORWARDED_FOR'):
                        ip = request.META.get("HTTP_X_FORWARDED_FOR")
                    else:
                        ip = request.META.get("REMOTE_ADDR")
                    # 对密码进行加盐
                    password_salt, password = Tools.password_encryption(password)
                    # 修改code 状态
                    goal_code = Code.objects.filter(cdk=code, state=1)[0]
                    goal_code.state = 0
                    goal_code.save()
                    # 创建对象
                    NormalUser.objects.create(email=username, password=password, password_salt=password_salt,
                                              registered_ip_address=ip, used_code=code)
                    # 添加日志
                    log_content = username + '进行了注册'
                    Log.objects.create(log_content=log_content)
            except:
                return redirect('/user/register/')

            return result
        else:
            return redirect('/user/register/')


# 获取验证码视图
def get_captcha_view(request):
    # 声明一个验证码对象
    img = ImageCaptcha()
    # 生成随机验证码 要从哪些字符串中取值 取多少位
    code = random.sample(string.digits + string.ascii_letters, 4)
    # 上步生成的是列表 需要进行拼接
    code = ''.join(code)
    print(code)
    # 将生成的验证码放入图片
    data = img.generate(code)
    # 将验证码存入session中
    request.session['true_captcha'] = code
    # 返回图片格式
    return HttpResponse(data, 'image/png')


# 定义登出页面
def log_out_view(request):
    # 获取session中用户名
    username = request.session.get('username', 'null')
    # 添加日志
    if username != 'null':
        log_content = username + '退出了登陆'
        Log.objects.create(log_content=log_content)
    # 清除session所有数据
    request.session.flush()
    result = redirect('/home/')
    # 删除cookie
    result.delete_cookie('password')
    result.delete_cookie('username')
    return result


