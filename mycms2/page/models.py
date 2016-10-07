from __future__ import unicode_literals
import bleach
from bs4 import BeautifulSoup
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from mycms2 import settings

class Page(MPTTModel):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique=True,\
            help_text=_('please input a-z or 0-9'))
    parent = TreeForeignKey('self', null=True, blank=True,\
            related_name='children', db_index=True, verbose_name=_('parent'))
    content = RichTextUploadingField(_('content'), null=True, blank=True)
    link = models.URLField(_('link'), blank=True, null=True)
    template = models.CharField(_('template'), max_length=50,\
            default='default')
    is_show = models.BooleanField(_('is show'), default=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __unicode__(self):
        return self.title

    def get_description(self, count=200):
        #return strip_tags(self.content)[0:200]
        return bleach.clean(strip_tags(self.content), strip=True)[0:count]

    def get_cover(self):
        tree = BeautifulSoup(self.content, "html5lib")
	cover  = tree.img
	if cover:
	    return cover['src']
	else:
	    return ''

    def get_link(self):
        if self.link:
            return self.link
        else:
            return 'http://%s/%s' % (settings.ALLOWED_HOSTS[0], self.slug)

    class Meta(object):
        verbose_name = _('page')
        verbose_name_plural = _('page')

    class MPTTMeta:
        order_insertion_by = ['title']
