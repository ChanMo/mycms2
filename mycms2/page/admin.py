from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Page

class PageAdmin(DraggableMPTTAdmin, admin.ModelAdmin):
    list_display = ('tree_actions', 'indented_title', 'template', 'is_show',\
            'created')
    list_filter = ('created', 'updated')
    list_display_links=('indented_title',)
    search_fields = ('title', 'intro')
    prepopulated_fields = {'slug': ('title',)}
    view_on_site = True
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content')
        }),
        ('More', {
            'classes': ('collapse',),
            'fields' : ('parent', 'template', 'link', 'is_show')
        }),
    )

    def view_on_site(self, obj):
        return obj.get_link()

admin.site.register(Page, PageAdmin)
