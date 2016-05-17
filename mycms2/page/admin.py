from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('full_title', 'slug', 'template', 'is_show', 'created')
    list_filter = ('created', 'updated')
    search_fields = ['title', 'intro']
    prepopulated_fields = {'slug': ('title',)}
    view_on_site = True
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content')
        }),
        ('More', {
            'classes': ('collapse',),
            'fields' : ('parent', 'cover', 'intro', 'sort', 'template', \
                    'is_show', 'link')
        }),
    )
    #date_hierarchy = 'created'
    empty_value_display = '-empty-'

    def view_on_site(self, obj):
        return 'http://localhost:8000/%s' % obj.slug

admin.site.register(Page, PageAdmin)
