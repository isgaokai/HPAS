from datetime import time

import re
import time

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from myLog.models import Log
from user.models import Administrator, NormalUser, Code

# Create your views here.
from Tools.Tools import Tools


# 用户管理主页面
def myAdmin_main_view(request):
    # 获取当前登陆用户类型
    user_type = request.session.get('user_type', 'null')

    # 管理员用户无法在主页面保存登陆状态
    # if user_type == 'normalUser' or user_type == 'null':
    # return redirect('/home/')
    # else:
    # 检测用户是否登陆
    now_user, username_head, username_tail = Tools.check_user_login(request)
    # 获取当前页面的索引
    page_index = int(request.GET.get('page_index', 1))
    # 查询全部职员
    users = NormalUser.objects.all()
    # 声明分页器对象
    paginator = Paginator(object_list=users, per_page=2)
    # 判断获取的页面索引是否超出范围
    if page_index not in paginator.page_range:
        # 如果超出范围则跳转回第一页
        page_index = 1
    # 当前页面对应的页面对象
    now_page = paginator.page(page_index)
    # 跳转到主html
    return render(request, 'admin_home.html', {'now_user': now_user,  # 当前登陆用户
                                               'username_head': username_head,  # 用户名头部
                                               'username_tail': username_tail,  # 用户名尾部
                                               'page': now_page
                                               })


# 管理员登陆页面
def myAdmin_login_view(request):
    # 返回对应页面
    return render(request, 'admin_login.html')


# 管理员登陆验证视图
def myAdmin_login_check_view(request):
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

    except:
        return redirect('/myAdmin/login/')
    print(username, password, captcha, true_captcha)

    # 正则及其他检验
    if not ePattern.search(username) and not mPattern.search(username):
        return HttpResponse('/myAdmin/login/')
    elif not pPattern.search(password) or Tools.checkout_password(password) == 'LowSecurity' or captcha != true_captcha:
        return HttpResponse('/myAdmin/login/')

    # 通过手机号登陆
    if mPattern.search(username):
        # 查询当前库内是否存在该用户
        if Administrator.objects.filter(phone=username).count() != 0:
            # 定位用户
            user = Administrator.objects.filter(phone=username)[0]
            # 对用户输入的密码与库内盐进行比对 检验密码是否正确
            password_salt, password = Tools.password_encryption(password, pwd_salt=user.password_salt)
            # 密码正确
            if password == user.password:
                # 返回响应
                result = redirect('/myAdmin/home/')
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
                # session添加登陆状态为'yes'
                request.session['logged_in'] = 'yes'
                # session添加用户名
                request.session['username'] = username
                # session添加用户类型
                request.session['user_type'] = 'admin'
                # 添加日志
                log_content = username + '管理员登陆了用户管理页面'
                Log.objects.create(log_content=log_content)
                # 返回
                return result
            else:
                return HttpResponse('/myAdmin/login/')
        else:
            return HttpResponse('/myAdmin/login/')
    # 通过email登陆
    else:
        # 查询当前库内是否存在该用户
        if Administrator.objects.filter(email=username).count() != 0:
            # 定位用户
            user = Administrator.objects.filter(email=username)[0]
            # 对用户输入的密码与库内盐进行比对 检验密码是否正确
            password_salt, password = Tools.password_encryption(password, pwd_salt=user.password_salt)
            # 密码正确
            if password == user.password:
                # 返回响应
                result = redirect('/myAdmin/home/')
                # 对用户的最后登陆时间进行修改
                user = Administrator.objects.filter(email=username)[0]
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

                # session添加登陆状态为'yes'
                request.session['logged_in'] = 'yes'
                # session添加用户名
                request.session['username'] = username
                # session添加用户类型
                request.session['user_type'] = 'admin'
                # 添加日志
                log_content = username + '管理员登陆了用户管理页面'
                Log.objects.create(log_content=log_content)
                # 返回
                return result
            else:
                return HttpResponse('/myAdmin/login/')
        else:
            return HttpResponse('/myAdmin/login/')


# 定义登出页面
def log_out_view(request):
    # 获取session中用户名
    username = request.session.get('username', 'null')
    # 添加日志
    if username != 'null':
        log_content = username + '管理员退出了登陆'
        Log.objects.create(log_content=log_content)
    # 清除session所有数据
    request.session.flush()
    result = redirect('/myAdmin/home/')
    # 删除cookie
    result.delete_cookie('password')
    result.delete_cookie('username')
    return result


# 新增用户页面
def myAdmin_adduser_view(request):
    # 获取当前登陆用户类型
    user_type = request.session.get('user_type', 'null')

    # 管理员用户无法在主页面保存登陆状态
    # if user_type == 'normalUser' or user_type == 'null':
    # return redirect('/home/')
    # else:
    # 检测用户是否登陆
    now_user, username_head, username_tail = Tools.check_user_login(request)
    if now_user:
        # 添加日志
        log_content = now_user + '管理员访问了新增用户页面'
        Log.objects.create(log_content=log_content)
    # 跳转到主html
    return render(request, 'admin_add_user.html', {'now_user': now_user,  # 当前登陆用户
                                                   'username_head': username_head,  # 用户名头部
                                                   'username_tail': username_tail,  # 用户名尾部

                                                   })


# 新增用户验证视图
def myAdmin_adduser_check_view(request):
    # 密码正则
    pPattern = re.compile(
        r'^[a-zA-Z0-9]\w{6,16/^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])|(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])|(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])).{6,}|(?:(?=.*[A-Z])(?=.*[a-z])|(?=.*[A-Z])(?=.*[0-9])|(?=.*[A-Z])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*[0-9])|(?=.*[a-z])(?=.*[^A-Za-z0-9])|(?=.*[0-9])(?=.*[^A-Za-z0-9])|).{6,16}$')
    # 邮箱正则
    ePattern = re.compile(r'^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$')
    # 手机号正则
    mPattern = re.compile(r'^((13[0-9])|(19[8])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$')

    try:
        # 接收用户输入昵称
        nickname = request.POST.get('txt_nickname')
        # 接收用户输入手机
        phone = request.POST.get('txt_phone')
        # 接收用户输入邮箱
        email = request.POST.get('txt_email')
        # 接收用户输入密码
        password = request.POST.get('txt_password')
        # 接收用户输入的第二次密码
        re_password = request.POST.get('txt_re_password')
        # 接收用户输入激活码
        code = request.POST.get('txt_code')

    except:
        return redirect('/myAdmin/home/')

    # 正则及其他检验
    if not ePattern.search(email) or not mPattern.search(phone):
        return redirect('/myAdmin/home/')
    elif not pPattern.search(password) or password != re_password or Tools.checkout_password(
            password) == 'LowSecurity' or len(code) != 12:
        return redirect('/myAdmin/home/')

    # 获取session中用户名
    username = request.session.get('username', 'null')

    # 进行添加用户
    if NormalUser.objects.filter(nickname=nickname).count() == 0:
        # 事务控制
        try:
            with transaction.atomic():
                # 返回响应
                result = redirect('/myAdmin/adduser/')
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
                NormalUser.objects.create(nickname=nickname, email=email, phone=phone, password=password,
                                          password_salt=password_salt,
                                          registered_ip_address=ip, used_code=code)
                # 添加日志
                if username != 'null':
                    log_content = str(username) + '管理员添加了用户:' + str(nickname) + '手机号:' + str(phone) + '邮箱号:' + str(
                        email)
                    Log.objects.create(log_content=log_content)
        except:
            return redirect('/myAdmin/adduser/')

        return result

    else:
        return redirect('/myAdmin/adduser/')
