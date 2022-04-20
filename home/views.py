from django.shortcuts import render

# Create your views here.

# 主页面试图函数
from Tools.Tools import Tools


def home_main_view(request):
    print(request.session.get('logged_in', 'no'))
    # 检测用户是否登陆
    now_user, username_head, username_tail = Tools.check_user_login(request)
    # 获取访问ip地址
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")
    print(ip)
    print(now_user,username_head,username_tail)
    # 跳转到主html
    return render(request,'home.html',{   'now_user': now_user,  # 当前登陆用户
                                          'username_head': username_head,  # 用户名头部
                                          'username_tail': username_tail,  # 用户名尾部
    })