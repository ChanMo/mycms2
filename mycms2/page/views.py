from django.http import HttpResponse
from django.template import Context, Template as TP
from .models import Page, Theme, Template

def get_template(template_name='index'):
    try:
        template = Template.objects.get(theme__is_actived=True,\
                name=template_name)
        return template.code
    except Template.DoesNotExist:
        return ''


def index(request):
    context = {
        'menu_list': Page.objects.root_nodes().filter(is_show=True),
    }
    template = TP(get_template())
    return HttpResponse(template.render(Context(context)))


def page(request, slug):
    page = Page.objects.get(slug=slug)
    context = {
        'page': page,
        'menu_list': Page.objects.root_nodes().filter(is_show=True),
        'children_list': page.get_children().filter(is_show=True),
        'sibling_list': page.get_siblings(include_self=True)\
                .filter(is_show=True)
    }
    template = TP(get_template(page.template))
    return HttpResponse(template.render(Context(context)))
