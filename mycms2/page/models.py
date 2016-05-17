#!/usr/bin/python
# vim: set fileencoding=utf8;
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey

class Page(MPTTModel):
    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(unique=True, verbose_name='链接名',\
            help_text='请输入唯一的链接名，可以包含数字，英文字母和下划线')
    parent = TreeForeignKey('self', null=True, blank=True,\
            related_name='children', db_index=True, verbose_name='父级')
    cover = models.ImageField(upload_to='page/%Y/%m/%d/',\
            verbose_name='封面', null=True, blank=True)
    intro = models.TextField(verbose_name='描述', null=True, blank=True)
    content = RichTextUploadingField(verbose_name='内容', null=True,\
            blank=True)
    link = models.URLField(blank=True, null=True, verbose_name='外部链接')
    template = models.CharField(max_length=50, default='default',\
            verbose_name='模板')
    sort = models.PositiveIntegerField(default=0, blank=False, null=False,\
            verbose_name='排序', help_text='数字越大越往前')
    is_show = models.BooleanField(default=True, verbose_name='是否显示')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.title

    def full_title(self):
        title = ''
        for item in self.get_ancestors():
            title += '---'
        title += ' ' + self.title
        return title

    def real_link(self):
        if self.link:
            return self.link
        else:
            return 'http://localhost:8000/%s' % self.slug

    class Meta(object):
        verbose_name = '页面'
        verbose_name_plural = '页面'

    class MPTTMeta:
        order_insertion_by = ['title']


