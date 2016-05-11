from django.views.generic import View, TemplateView
from mycms2 import settings
from .models import Page

theme = settings.THEME

class BaseView(View):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['menu_list'] = Page.objects.root_nodes().order_by('sort')
        return context

class HomeView(BaseView, TemplateView):
    template_name = theme+'/index.html'

class PageView(BaseView, TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page = Page.objects.get(slug=self.kwargs['slug'])
        self.page = page
        context['page'] = page
        context['children_list'] = self.page.get_children().\
                filter(is_show=True).order_by('-sort')
        context['sibling_list'] = self.page.get_siblings(include_self=True).\
                filter(is_show=True).order_by('-sort')
        return context

    def get_template_names(self, **kwargs):
        return theme+'/%s.html' % self.page.template
