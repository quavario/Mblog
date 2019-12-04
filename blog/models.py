import os
import uuid

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


# 上传文件路径
def content_file_name(instance, filename):
    print(instance)
    print(type(instance))
    uuid_name = uuid.uuid4().__str__().replace('-', '')
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid_name, ext)
    return os.path.join(instance.path, filename)


# Create your models here.
class Post(models.Model):
    path = 'post'
    title = models.CharField(max_length=256, db_index=True, verbose_name='标题')
    sub_title = models.CharField(max_length=1024, null=True, blank=True, verbose_name='子标题')
    # 缩略图
    thumb = models.ImageField(upload_to=content_file_name, null=True, blank=True, verbose_name='缩略图')
    content = RichTextUploadingField(verbose_name='内容', null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    create_by = models.IntegerField(verbose_name='创建人')
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    update_by = models.IntegerField(verbose_name='更新人')
    order = models.IntegerField(default=0, verbose_name='排序')
    status = models.IntegerField(default=0, verbose_name='状态')

    class Meta:
        verbose_name_plural = '文章'
        verbose_name = '文章'

    def __str__(self):
        return self.title

    def edit(self):
        return '编辑'

    edit.short_description = '操作'

    def username(self):
        user = User.objects.get(id=self.create_by)
        return user.username

    username.admin_order_field = 'create_by'
    username.short_description = '创建人'


class Config(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    value = models.CharField(max_length=256, )
    type = models.IntegerField(db_index=True)
