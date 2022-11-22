from django import template
from blog.models import Post, Hashtag
from django.db.models import Count


register = template.Library()

@register.inclusion_tag('shared/footer.html')
def footer_view():
    end_posts = Post.objects.published()[:4]
    best_tag = Hashtag.objects.all().annotate(count=Count('post')).order_by('-count').distinct()[:7]
    return {
        'end_posts': end_posts,
        'best_tag': best_tag
    }


@register.inclusion_tag('account/partials/link.html')
def link(request, link_name, content, icon):
    return {
        'request': request,
        'link_name': link_name,
        'link': 'account:{}'.format(link_name),
        'content': content,
        'icon' : icon
    }
