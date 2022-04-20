# -*- encoding : utf-8 -*-
# @Project -> File     ：HPAS -> urls         
# @IDE      ：PyCharm
# @Author   ：Fenglchen
# @Date     ：2022/4/4 10:07 上午
# @Software : macos python3.8
from django.urls import re_path, path

from home import views

app_name = 'home'

urlpatterns = [
    # 主页面
    path('',views.home_main_view,name='home_main_view'),
]