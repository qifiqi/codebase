from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
"""
先写普通字段
再写外键字段
"""


class UserInfo(AbstractUser):
    phone = models.BigIntegerField(verbose_name="手机号", null=True, blank=True)
    """
    null=True 数据库可以为空
    blank=True 后台管理可以为空
    """

    # 头像
    avatar = models.FileField(upload_to="avatar/", default="avatar/default.png", verbose_name="用户头像")
    # 设置文件保存地址，如果没有就设置默认头像

    create_time = models.DateField(auto_now_add=True)

    blog = models.OneToOneField(to="Blog", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "用户表"


class Blog(models.Model):
    site_name = models.CharField(verbose_name="站点名称", max_length=32)
    site_title = models.CharField(verbose_name="站点标题", max_length=32)
    site_theme = models.CharField(verbose_name="站点样式", max_length=64)  # 存储css、js路径

    def __str__(self):
        return self.site_name


class Category(models.Model):
    name = models.CharField(verbose_name="文章分类", max_length=32)

    blog = models.ForeignKey(to="Blog", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name="文章标签", max_length=32)

    blog = models.ForeignKey(to="Blog", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name="文章标题", max_length=64)
    desc = models.CharField(verbose_name="文章简介", max_length=255)
    # 文章内容有很多，一般情况下都是使用TextFiled()
    content = models.TextField(verbose_name="文章内容")

    create_time = models.DateField(auto_now_add=True)

    up_num = models.BigIntegerField(default=0, verbose_name="点赞数")
    down_num = models.BigIntegerField(default=0, verbose_name="点踩数")
    comment_num = models.BigIntegerField(default=0, verbose_name="评论数")

    # 外键
    blog = models.ForeignKey(to="Blog", on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE, null=True)

    tags = models.ManyToManyField(
        to="Tag",
        through="Article2Tag",
        through_fields=("article", "tag")
    )

    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    article = models.ForeignKey(to="Article", on_delete=models.CASCADE)
    tag = models.ForeignKey(to="Tag", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.article}:{self.tag}"

class UpAndDown(models.Model):
    user = models.ForeignKey(to="UserInfo", on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(to="Article", on_delete=models.SET_NULL, null=True)
    is_up = models.BooleanField()


class Comment(models.Model):
    user = models.ForeignKey(to="UserInfo", on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(to="Article", on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=32, verbose_name="评论内容")
    comment_time = models.DateTimeField(auto_now_add=True)
    # 自关联
    parent = models.ForeignKey(to="self", on_delete=models.CASCADE,null=True)
