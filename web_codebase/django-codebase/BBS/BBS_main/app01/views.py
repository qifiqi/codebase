import random
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from app01.app01_forms import MyRegForm
from app01 import models
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO, StringIO
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import TruncMonth


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
                back_dic["url"] = redirect("app01_home").url
            else:
                back_dic["code"] = 402
                back_dic["msg"] = "用户名或者密码错误"
        else:
            back_dic["code"] = 403
            back_dic["msg"] = "验证码错误"
        print(back_dic)
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

    # 1.查询当前用户所有的分类及分类小的文章数
    category_list = models.Category.objects.filter(blog=blog).annotate(
        count_name=Count("article__pk")
    ).values("pk", "name", "count_name")

    # 2.差早当前用户所有的标签和标签数
    tag_list = models.Tag.objects.filter(blog=blog).annotate(
        count_name=Count("article__pk")
    ).values("pk", "name", "count_name")

    # 3.更加年月份分组统计
    data_list = models.Article.objects.filter(blog=blog).annotate(
        month=TruncMonth("create_time")).values("month").annotate(
        count_name=Count("pk")).values("month", "count_name")

    return render(requests, "app01/site.html", locals())
