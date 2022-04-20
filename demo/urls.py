# -*- encoding : utf-8 -*-
# @Project -> File     ：HPAS -> urls
# @IDE      ：PyCharm
# @Author   ：Fenglchen
# @Date     ：2022/4/7 9:50 上午
# @Software : macos python3.8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bar/$', views.ChartView.as_view(), name='demo'),
    url(r'^index/$', views.IndexView.as_view(), name='demo'),
]