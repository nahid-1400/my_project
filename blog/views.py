from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from .models import Post
import itertools
from .models import CateGory
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

   
def home_view(request):
    posts = Post.objects.published()[:4]
    my_grouper_post = my_grouper(2, posts)
    context = {'posts': my_grouper_post, 'title': 'خانه'}
    return render(request, 'blog/index.html', context)

# class PostList(ListView):
#     # model = Post
#     template_name = 'blog/index.html' # or change name index.html to article_list.html
#     # context_object_name = 'queryset' # or using of  object_list in templat
#     queryset = Post.objects.published()[:4]
#     posts = my_grouper(2, queryset)
#
#     # paginate_by = 3



# def detail(request, slug, id):
#     context = {
#        'post': get_object_or_404(Post.objects.published(), slug=slug, id=id),
#        'title': 'پست'
#     }
#     return render(request, 'blog/single-post.html', context)
#

class DetailClass(DetailView):
    template_name = 'blog/single-post.html'  #or change name template to article_detail.html
    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post.objects.published(), slug=slug, id=id)

# def category_view(request, slug, page=1):
#     category = get_object_or_404(CateGory.objects.category_status(slug))
#     paginator_post = Paginator(category.post_category.all(), 1)
#     page_obj = paginator_post.get_page(page)
#
#     context = {
#         'posts': page_obj,
#         'category': category,
#         'title': 'دسته بندی',
#     }
#     return render(request, 'blog/article_category.html', context)

class ArticleCateGoryList(ListView):
    paginate_by = 2
    template_name = 'blog/article_category.html'
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(CateGory.objects.category_status(slug))
        return category.post_category.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = category
        return context

class CateGoryList(ListView):
    paginate_by = 5
    template_name = 'blog/category.html'
    def get_queryset(self):
        category = CateGory.objects.category_active()
        return category

class AuthorList(ListView):
    paginate_by = 2
    template_name = 'blog/author_page.html'
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['author'] = author
        return context
