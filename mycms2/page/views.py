from django.views.generic import View, TemplateView
from mycms2 import settings
from .models import Page

theme = settings.THEME

class BaseView(View):
    """
    BaseView, render menu list to templates
    """
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['menu_list'] = Page.objects.root_nodes().\
                filter(is_show=True).order_by('title')
        return context

class HomeView(BaseView, TemplateView):
    """
    HomeView
    """
    template_name = '%s/index.html' % theme

class PageView(BaseView, TemplateView):
    """
    PageView
    """
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page = Page.objects.get(slug=self.kwargs['slug'])
        self.page = page
        context['page'] = page
        context['children_list'] = self.page.get_children().\
                filter(is_show=True)
        context['sibling_list'] = self.page.get_siblings(include_self=True).\
                filter(is_show=True)
        return context

    def get_template_names(self, **kwargs):
        return '%s/%s.html' % (theme, self.page.template)
