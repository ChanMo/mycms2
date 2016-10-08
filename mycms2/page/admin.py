from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Theme, Template, Page
from mycms2.widgets import HtmlEditor

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_actived', 'created')
    prepopulated_fields = {'value': ('name',)}

class TemplateForm(forms.ModelForm):
    model = Template
    class Meta:
        fields = '__all__'
        widgets = {
            'code': HtmlEditor(),
        }

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('theme', 'name', 'created')
    list_filter = ('theme', 'created', 'updated')
    form = TemplateForm

class PageAdmin(DraggableMPTTAdmin, admin.ModelAdmin):
    list_display = ('tree_actions', 'indented_title', 'template', 'is_show',\
            'created')
    list_filter = ('created', 'updated')
    list_display_links=('indented_title',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    view_on_site = True
    fieldsets = (
        (None, {
            'fields': ('parent', 'title', 'slug', 'content', 'template')
        }),
        (_('more'), {
            'classes': ('collapse',),
            'fields' : ('link', 'is_show')
        }),
    )

    def view_on_site(self, obj):
        return obj.get_link()

admin.site.register(Page, PageAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Template, TemplateAdmin)
