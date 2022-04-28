from django.shortcuts import render, redirect

# Create your views here.

from Tools.Tools import Tools

# 主页面
def home_main_view(request):
    # 获取当前登陆用户类型
    user_type =  request.session.get('user_type', 'null')
    # 获取当前登陆用户ID
    now_user_id = request.session.get('now_user_id', '-1')

    # 管理员用户无法在主页面保存登陆状态
    if user_type == 'admin' or user_type == 'null':
        now_user, username_head, username_tail = None,None,None
    else:
        # 检测用户是否登陆
        now_user, username_head, username_tail = Tools.check_user_login(request)

    # 跳转到主html
    return render(request,'home.html',{   'now_user': now_user,  # 当前登陆用户
                                          'username_head': username_head,  # 用户名头部
                                          'username_tail': username_tail,  # 用户名尾部
                                          'now_user_id':now_user_id # 当前登陆用户ID
    })
