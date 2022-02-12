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

