from django import template
from ..models import CateGory


register = template.Library()

@register.inclusion_tag('shared/Header.html')
def header_view():
    category = CateGory.objects.filter(status=True)
    context = {'category': category}
    return context


@register.inclusion_tag('shared/footer.html')
def footer_view():
    pass

@register.inclusion_tag('registration/partials/link.html')
def link(request, link_name, content, icon):
    return {
        'request': request,
        'link_name': link_name,
        'link': 'account:{}'.format(link_name),
        'content': content,
        'icon' : icon
    }
