import json
import time
import os.path
import random
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse
from app01.app01_forms import MyRegForm
from app01 import models
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO, StringIO
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.db.models import F
from django.db import transaction
from utils.app01_page import Pagination
from bs4 import BeautifulSoup
from BBS_main import settings


# Create your views here.
# 注册
def register(requests):
    """
    注册模块
    :param requests:
    :return:
    """
    form_obj = MyRegForm()
    if requests.method == "POST":
        back_dict = {"code": 200, "msg": ""}

        # 校验数据是否合法
        form_obj = MyRegForm(requests.POST)
        if form_obj.is_valid():

            # 将数据另存
            cleaned_data = form_obj.cleaned_data
            # 将两次密码删除一个
            cleaned_data.pop("confirm_password")
            # 获取文件对象
            file_obj = requests.FILES.get("avatar")
            # 判断是否有值
            if file_obj:
                cleaned_data["avatar"] = file_obj
            # 操作数据库保存
            models.UserInfo.objects.create_user(**cleaned_data)
            back_dict["url"] = redirect("login").url

        else:

            back_dict["code"] = 2000
            back_dict["msg"] = form_obj.errors

        return JsonResponse(back_dict)
    return render(requests, "app01/register.html", locals())


# 登录
def login(requests):
    """
    登录验证模块
    :param requests:
    :return:
    """
    if requests.method == "POST":
        back_dic = {"code": 200, "msg": ""}
        username = requests.POST.get("username")
        password = requests.POST.get("password")
        id_code = requests.POST.get("id_code")
        if requests.session.get("code").upper() == id_code.upper():
            # 校验账号密码是否正确
            user_obj = auth.authenticate(requests, username=username, password=password)
            if user_obj:
                # 保存用户状态
                auth.login(requests, user_obj)
                back_dic["url"] = reverse("home")
            else:
                back_dic["code"] = 402
                back_dic["msg"] = "用户名或者密码错误"
        else:
            back_dic["code"] = 403
            back_dic["msg"] = "验证码错误"
        return JsonResponse(back_dic)
    return render(requests, "app01/login.html")


# 修改密码
@login_required
def ser_password(requests):
    if requests.is_ajax():
        back_dict = {"code": 200, "msg": ""}
        if requests.method == "POST":
            old_password = requests.POST.get("old_password")
            new_password = requests.POST.get("new_password")
            confirm_password = requests.POST.get("confirm_password")
            is_right = requests.user.check_password(old_password)
            print(is_right, old_password)
            if is_right:
                if new_password == confirm_password:
                    requests.user.set_password(new_password)
                    requests.user.save()
                    back_dict["msg"] = "ok"
                else:
                    back_dict["code"] = 1001
                    back_dict["msg"] = "两次密码不正确"
            else:
                back_dict["code"] = 1002
                back_dict["msg"] = "与原密码不正确"
        return JsonResponse(back_dict)
    return HttpResponse("ser_password")


# 退出登录
def logout(requests):
    auth.logout(requests)
    return redirect("login")


# 生成RGB颜色
def get_random_rgb():
    """
    生成一个随机的RGB颜色
    :return:
    """
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# 获取验证码
def get_code(requests):
    """
    随机验证码
    :param requests:
    :return:
    """
    # 利用pillow模块产生图片
    img_obj = Image.new("RGB", (480, 35), get_random_rgb())
    img_draw = ImageDraw.Draw(img_obj)
    img_font = ImageFont.truetype("static/app01/fonts/雷鬼One.ttf", 30)  # 样式和大小

    code = ""
    for i in range(6):
        # 大写字母
        random_upper = chr(random.randint(65, 90))
        # 小写字母
        random_lower = chr(random.randint(97, 122))
        # 数字
        random_num = str(random.randint(0, 9))
        # 从三个中随机选择一个
        tmp = random.choice([random_num, random_lower, random_upper])
        # 将产生的随机字符串写入图片
        # 一个个写可以控制间隙，一次性写无法控制
        img_draw.text((i * 50, 0), tmp, get_random_rgb(), img_font)  # 位置，文字，颜色，字体样式
        code += tmp
    # 随机字符串要在登录的时候使用到，要对比，所以要找一个地方存下来
    print(code)
    requests.session["code"] = code
    io_obj = BytesIO()
    img_obj.save(io_obj, "png")
    return HttpResponse(io_obj.getvalue())


# 主页
def home(requests):
    # 查询本网站下所有文章数据，
    article_queryset = models.Article.objects.all()

    # 分页
    page_obj = Pagination(
        current_page=requests.GET.get("page", 1),
        all_count=article_queryset.count(),
        per_page_num=10,
    )
    page_queryset = article_queryset[page_obj.start:page_obj.end]

    return render(requests, "app01/home.html", locals())


# 个人站点
def site(requests, username, **kwargs):
    """

    :param requests:
    :param username:
    :param kwargs: 如果改参数有就是要做额为的筛选
    :return:
    """
    # 先校验当前用户名对应的个人站点是否存在
    user_obj = models.UserInfo.objects.filter(username=username).first()
    # 若不存在404
    if not user_obj:
        return render(requests, "error_404.html")
    blog = user_obj.blog
    # 查询个人站点下的所有文章
    article_list = models.Article.objects.filter(blog=blog)
    # 判断是否有参数
    if kwargs:
        condition = kwargs.get("condition")
        param = kwargs.get("param")
        # 判断用户筛选的条件
        if condition == "category":
            # 查分类
            article_list = article_list.filter(category_id=param)
        elif condition == "tag":
            # 查出标签id 多对多
            article_list = article_list.filter(tags__id=param)
        elif condition == "archive":
            year, month = param.split("-")
            # 查时间
            article_list = article_list.filter(create_time__year=year, create_time__month=month)
        else:
            return render(requests, "error_404.html")

    # # 1.查询当前用户所有的分类及分类小的文章数
    # category_list = models.Category.objects.filter(blog=blog).annotate(
    #     count_name=Count("article__pk")
    # ).values("pk", "name", "count_name")
    #
    # # 2.差早当前用户所有的标签和标签数
    # tag_list = models.Tag.objects.filter(blog=blog).annotate(
    #     count_name=Count("article__pk")
    # ).values("pk", "name", "count_name")
    #
    # # 3.更加年月份分组统计
    # data_list = models.Article.objects.filter(blog=blog).annotate(
    #     month=TruncMonth("create_time")).values("month").annotate(
    #     count_name=Count("pk")).values("month", "count_name")

    # 分页
    page_obj = Pagination(
        current_page=requests.GET.get("page", 1),
        all_count=article_list.count(),
        per_page_num=10,
    )
    page_queryset = article_list[page_obj.start:page_obj.end]

    return render(requests, "app01/site.html", locals())


# 文章详情
def article_detail(requests, username, article_id):
    """
    应该校验username和article_id是否存在，
    :param requests:
    :param username:用户名
    :param article_id:文章id
    :return:
    """

    article_obj = models.Article.objects.filter(pk=article_id, blog__userinfo__username=username).first()
    if not article_obj:
        return render(requests, "error_404.html")

    user_obj = models.UserInfo.objects.filter(username=username).first()
    blog = user_obj.blog

    # 获取当前文章的所有评论内容

    comment_list = models.Comment.objects.filter(article=article_obj)

    return render(requests, "app01/article_detail.html", locals())

    pass


# 点赞和点踩
def up_or_down(requests):
    """
    1.校验登录
    2. 自己不能给自己点
    3。只能点一次
    4.操作数据库
    点赞点擦的处理
    :param requests:
    :return:
    """
    if requests.is_ajax():
        back_dict = {"code": 200, "msg": ""}

        # 判断是否登录
        if requests.user.is_authenticated:
            article_id = requests.POST.get("article_id")
            is_up = json.loads(requests.POST.get("is_up"))

            # 判断是否是自己写的
            article_obj = models.Article.objects.filter(pk=article_id).first()
            if not article_obj.blog.userinfo == requests.user:

                # 校验用户是否已经点过
                is_click = models.UpAndDown.objects.filter(user=requests.user, article=article_obj)
                if not is_click:

                    # 操作数据库 ,要同步操作
                    # 判断是点赞还是点擦
                    if is_up:
                        # 给点赞增加一
                        models.Article.objects.filter(pk=article_id).update(up_num=F("up_num") + 1)
                        back_dict["msg"] = "点赞成功"
                        pass
                    else:
                        # 给点擦加一
                        models.Article.objects.filter(pk=article_id).update(down_num=F("down_num") + 1)
                        back_dict["msg"] = "点踩成功"
                    # 操作表
                    models.UpAndDown.objects.create(user=requests.user, article=article_obj, is_up=is_up)
                else:
                    # 校验用户是否已经点过
                    back_dict["code"] = 2001
                    back_dict["msg"] = "你已经点过l"
            else:
                # 判断是否是自己写的
                back_dict["code"] = 2002
                back_dict["msg"] = "不可以点自己"
        else:
            # 判断是否登录
            back_dict["code"] = 2003
            back_dict["msg"] = '<a href="/login/">要登录哦</a>'
        return JsonResponse(back_dict)


# 文章评论
def article_comment(requests):
    """
    自己可以给自己评论
    :param requests:
    :return:
    """
    back_dict = {"code": 200, "msg": ""}
    if requests.is_ajax():
        if requests.method == "POST":
            if requests.user.is_authenticated:
                article_id = requests.POST.get("article_id")
                parentId = requests.POST.get("parentId")
                comment = requests.POST.get("comment")
                # 直接操作评论表存储数据,动两张表
                # 开启事务
                with transaction.atomic():
                    models.Article.objects.filter(pk=article_id).update(comment_num=F("comment_num") + 1)
                    models.Comment.objects.create(
                        user=requests.user,
                        article_id=article_id,
                        content=comment,
                        parent_id=parentId
                    )
                back_dict["msg"] = "评论成功"
            else:
                back_dict["code"] = 2001
                back_dict["msg"] = "用户未登录"

        return JsonResponse(back_dict)


@login_required
def backend(requests):
    """
    后台
    :param requests:
    :return:
    """
    article_list = models.Article.objects.filter(blog=requests.user.blog)
    # 分页
    page_obj = Pagination(
        current_page=requests.GET.get("page", 1),
        all_count=article_list.count(),
        per_page_num=10,
    )
    page_queryset = article_list[page_obj.start:page_obj.end]

    return render(requests, "app01/app10_backend/backend.html", locals())


@login_required
def backend_add_article(requests):
    category_list = models.Category.objects.filter(blog=requests.user.blog)
    tag_list = models.Tag.objects.filter(blog=requests.user.blog)

    if requests.method == "POST":
        title = requests.POST.get("title")
        content = requests.POST.get("content")
        category_id = requests.POST.get("category")
        tag_list = requests.POST.getlist("tag")
        # 模块使用
        soup = BeautifulSoup(content, "html.parser")
        # 获取所有的标签
        tags = soup.find_all()

        # 处理标签
        for tag in tags:
            if tag.name == "script":
                # 是就删除
                tag.decompose()
        # 文章简介
        # 暴力截取所有
        # desc = content[:150]
        # 2.获得全部文本再截取
        desc = soup.text[:150]

        article_obj = models.Article.objects.create(
            title=title,
            content=str(soup),
            desc=desc,
            category_id=category_id,
            blog=requests.user.blog
        )

        # 文章标签表示自己创建的是用不了ORM自带的add，remove，clear
        # 自己操作 一次数据创建多

        # 使用批量插入 bulk_create()
        article_obj_list = []
        # 生成多个文章对应标签的对象
        for i in tag_list:
            article_obj_list.append(
                models.Article2Tag(article=article_obj, tag_id=i)
            )
        # 批量插入
        models.Article2Tag.objects.bulk_create(article_obj_list)
        # 跳转到文章后台管理
        return redirect(reverse("backend"))

    return render(requests, "app01/app10_backend/backend_add_article.html", locals())


# 编辑器上传文件
def upload_img(requests):
    """
    返回格式限制
    //成功时
{
        "error" : 0,
        "url" : "http://www.example.com/path/to/file.ext"
}
//失败时
{
        "error" : 1,
        "message" : "错误信息"
}
    :param requests:
    :return:
    """
    back_dict = {
        "error": 0,
        # "url":"static/app01/img/default.png"
    }  # 提前定义数据格式
    if requests.method == "POST":
        # 获取用户上传的图片数据
        file_obj = requests.FILES.get("imgFile")
        # 手动拼接存储路径
        file_dir = os.path.join(settings.BASE_DIR, "media", "article_img")
        # 优化操作
        # 判断是否存在不存在创建
        if not os.path.isdir(file_dir):
            os.mkdir(file_dir)
        # 做图片名称处理
        img_file = "_".join((str(requests.user.pk), str(int(time.time())), file_obj.name))
        # 拼接图片完整路径
        file_path = os.path.join(file_dir, img_file)
        with open(file_path, "wb") as f:
            for line in file_obj:
                f.write(line)

        back_dict["url"] = f"media/article_img/{img_file}"

        return JsonResponse(back_dict)


# 修改用户头像
@login_required
def set_avatar(requests):
    """

    :param requests:
    :return:
    """
    if requests.method == "POST":
        img_file_obj = requests.FILES.get("avatar")
        # 这个不会写到数据库中文件只会是文件名，没有路径
        # models.UserInfo.objects.filter(pk=requests.user.pk).update(avatar=img_file_obj)
        # 解决办法
         # 1.自己拼接
        # 2.换一种更新
        user_obj = requests.user
        user_obj.avatar = img_file_obj
        user_obj.save()
        return redirect(reverse("home"))
    return render(requests,"app01/app10_backend/set_avatar.html",locals())

    pass
