from datetime import datetime

from django.db import models


# 列表详情
class steam(models.Model):
    appid = models.CharField('应用id', max_length=30)
    publishedfileid = models.CharField('项目id', max_length=40, primary_key=True)
    grade = models.CharField('等级', max_length=1)
    title = models.CharField('标题', max_length=300)
    author = models.CharField('作者', max_length=100)
    href = models.CharField('地址', max_length=300)
    img_path = models.CharField('图片地址', max_length=300)
    type = models.CharField('类型', max_length=50)
    datatime = models.DateTimeField('创建时间', default=datetime.now())

    def toDict(self):
        return {
            'appid': self.appid,
            'publishedfileid': self.publishedfileid,
            'grade': self.grade,
            'title': self.title,
            'author': self.author,
            'href': self.href,
            'img_path': self.img_path,
            'type': self.type,
        }
    class Meta:
        db_table='steam'