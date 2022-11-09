from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path("set_password/", views.ser_password, name="ser_password"),

    # 图片验证码相关
    path("get_code/", views.get_code, name="get_code"),

    # 个人站点
    re_path("^(?P<username>\w+)/$", views.site, name="site"),
    # 侧边栏筛选
    # re_path("(?P<username>\w+)/category/(\d+)/", views.site),
    # re_path("(?P<username>\w+)/tag/(\d+)/", views.site),
    # re_path("(?P<username>\w+)/archive/(\w+)/", views.site),
    # 合并上面三条url
    re_path("^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)/", views.site),

]
