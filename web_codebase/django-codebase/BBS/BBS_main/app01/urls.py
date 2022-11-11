from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path("set_password/", views.ser_password, name="ser_password"),

    # 图片验证码相关
    path("get_code/", views.get_code, name="get_code"),

    # 文章评论
    path("article_comment/", views.article_comment, name="article_comment"),
    # 文章修改
    path("backend/", views.backend, name="backend"),
    path("backend/add/article", views.backend_add_article, name="backend_add_article"),

    # 编辑器上传图片
    path("backend/upload_img", views.upload_img, name="upload_img"),

    # 修改用户头像
    path("set/avatar", views.set_avatar, name="set_avatar"),

    # 个人站点
    path("<str:username>/", views.site, name="site"),
    # 侧边栏筛选
    # re_path("(?P<username>\w+)/category/(\d+)/", views.site),
    # re_path("(?P<username>\w+)/tag/(\d+)/", views.site),
    # re_path("(?P<username>\w+)/archive/(\w+)/", views.site),
    # 合并上面三条url
    re_path("^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)/", views.site),

    path("<str:username>/article/<int:article_id>", views.article_detail, name="article_detail"),

    # 点赞点擦
    path("up_or_down/", views.up_or_down, name="up_or_down"),


]
