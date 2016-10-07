from django.utils.translation import ugettext_lazy as _
from django.db import models

class Group(models.Model):
    name = models.CharField(_('name'), max_length=200)
    created = models.DateTimeField(_('created time'), auto_now_add=True)
    updated = models.DateTimeField(_('updated time'), auto_now=True)
    def __unicode__(self):
        return self.name

    class Meta(object):
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class Banner(models.Model):
    group = models.ForeignKey(Group, related_name='banners',\
            verbose_name=_('group'))
    title = models.CharField(_('name'), max_length=200)
    image = models.ImageField(_('image'), upload_to='upload/banner/%Y/%m/%d')
    link = models.URLField(_('link'), blank=True, null=True)
    sort = models.PositiveIntegerField(_('sort'), default=0, blank=False,\
            null=False)
    created = models.DateTimeField(_('created time'), auto_now_add=True)
    updated = models.DateTimeField(_('updated time'), auto_now=True)
    is_show = models.BooleanField(_('is_show'), default=True)

    def unicode(self):
        return self.title

    def image_url(self):
        return '<img src="%s" height="50px">' % self.image.url

    class Meta(object):
        ordering = ['sort']
        verbose_name = _('banner')
        verbose_name_plural = _('banners')

    image_url.allow_tags = True
    image_url.short_description = _('image')
