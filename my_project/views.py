from blog.models import CateGory, Post, Hashtag
from django.shortcuts import render
from django.db.models import Count



def header_view(request):
    category = CateGory.objects.filter(status=True)
    post_is_special = Post.objects.filter(is_special=True)[:5]
    new_post = Post.objects.published()[:3]
    purpal_Tag = Hashtag.objects.all().annotate(count=Count('hits')).order_by('-count').distinct()[:5]
    context = {'category': category,
               'post_is_special': post_is_special,
               'new_post': new_post, 'purpal_Tag': purpal_Tag
               }
    return render(request, 'shared/Header.html', context)