"""HPAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, re_path, include
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 设置静态资源
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # home_app
    re_path(r'^$',home_views.home_main_view,name='home_main_view'),
    path('home/', include('home.urls')),
    # user_app
    path('user/', include('user.urls')),
    # ajax_app
    path('ajax/', include('ajax.urls')),
    # demo
    url(r'^demo/', include('demo.urls')),
]
