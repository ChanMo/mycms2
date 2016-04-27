from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import *

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    list_filter = ('created',)
    list_per_page = 20
    search_fields = ['name']

class BannerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('group', 'title', 'image_url', 'created', 'is_show')
    list_display_links = ('group',)
    list_filter = ('is_show',)
    list_per_page = 20
    search_fields = ['title']

admin.site.register(Group, GroupAdmin)
admin.site.register(Banner, BannerAdmin)
