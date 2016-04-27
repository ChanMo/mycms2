#!/usr/bin/python
# vim: set fileencoding=utf-8 :
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name='名称')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    def __unicode__(self):
        return self.name

    class Meta(object):
        verbose_name = '分组'
        verbose_name_plural = '分组'


class Banner(models.Model):
    group = models.ForeignKey(Group, related_name='banners', verbose_name='分组')
    title = models.CharField(max_length=200, verbose_name='标题')
    image = models.ImageField(upload_to='upload/banner/%Y/%m/%d',\
                              verbose_name='图片')
    link = models.URLField(verbose_name='链接', blank=True, null=True)
    sort = models.PositiveIntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_show = models.BooleanField(default=False, verbose_name='是否显示')

    def unicode(self):
        return self.title

    def image_url(self):
        return '<img src="%s" height="50px">' % self.image.url

    class Meta(object):
        ordering = ['sort']
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

    image_url.allow_tags = True
    image_url.short_description = '图片'
