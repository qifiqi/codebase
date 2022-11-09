"""BBS_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from app01 import views
from django.views.static import serve
from BBS_main import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('app01/', include("app01.urls"), name="app01"),

    # 登录注销
    path('login/', views.login, name="login"),
    path("logout/", views.logout, name="logout"),

    # 注册
    path("register/", views.register, name="register"),
    # 首页
    path("home/", views.home, name="home"),
    # 开设后端接口
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]
