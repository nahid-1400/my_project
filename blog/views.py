from account.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Slider, Hashtag
import itertools
from .models import CateGory
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from account.mixins import AuthorAccessArticleMixin
from django.db.models import Q
from django.db.models import Count
from comment.models.comments import Comment
import datetime

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def about_us(request):
    return render(request, 'blog/about_us.html', {'title' : 'درباره ما'})
   
def home_view(request):
    admin = User.objects.get(is_superuser=True)
    posts = Post.objects.published()[:4]
    all_post = Post.objects.published()
    my_grouper_post = my_grouper(2, posts)
    sliders = Slider.objects.filter(active=True)[:1]
    purpal_news = Post.objects.order_by('-like_user').distinct()[:6]
    hot_news = Post.objects.published().annotate(count=Count('hits', filter=Q(comments__content_type_id=7))).order_by('-count').distinct()[:6]
    comments = Comment.objects.all().distinct()[:6]
    best_news = Post.objects.published().annotate(count=Count('hits')).order_by('-count').distinct()[:4]
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    best_news_last_week = Post.objects.filter(published_time__range=[last_week, datetime.date.today()]).order_by('-hits', '-published_time').distinct()[:4]
    best_tag = Hashtag.objects.all().annotate(count=Count('post')).order_by('-count').distinct()[:10]
    count_like = 0
    for posts in all_post.all():
        for likes in posts.like_user.all():
            count_like += 1
    context = {'posts': my_grouper_post, 'all_post': all_post,
               'title': 'خانه', 'sliders': sliders, 'count_like' : count_like,
               'purpal_news': purpal_news, 'hot_news': hot_news, 'comments': comments, 'best_news': best_news,
               'best_news_last_week' :best_news_last_week, 'best_tag': best_tag, 'admin' : admin
 }
    return render(request, 'blog/index.html', context)




class DetailClass(DetailView):
    template_name = 'blog/single-post.html'  #or change name template to article_detail.html

    def get_object(self, queryset=None):
        global post
        id = self.kwargs.get('id')
        slug = self.kwargs.get('slug')
        post = get_object_or_404(Post.objects.published(), slug=slug, id=id)
        ip = self.request.user.ip_address
        if ip not in post.hits.all():
            post.hits.add(ip)
            post.save()
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['new_post'] = Post.objects.published()[1:6]
        context['end_news'] = Post.objects.published().first()
        context['related_post'] = Post.objects.get_queryset().filter(category__post_category=post).distinct()[:2]
        return context



class ArticlePreview(AuthorAccessArticleMixin, DetailView):
    template_name = 'blog/single-post.html'
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post.objects, slug=slug, pk=pk)

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
        end_news1 = Post.objects.published()[:1]
        end_news2 = Post.objects.published()[1:3]
        context['category'] = category
        context['end_news1'] = end_news1
        context['end_news2'] = end_news2
        return context




class Search(ListView):
    paginate_by = 10
    template_name = 'blog/all_post_search.html'

    def get_queryset(self):
        global q, posts
        q = self.request.GET.get('q')
        return Post.objects.filter(Q(title__icontains=q)|Q(description__icontains=q))


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        all_post = Post.objects.published()
        context['q'] = q
        context['all_post'] = all_post
        return context

class AllPost(ListView):
    paginate_by = 10
    template_name = 'blog/all_post_search.html'
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        all_post = Post.objects.published().distinct()
        new_post = Post.objects.order_by('-id').distinct()
        purpal_news = Post.objects.order_by('-like_user').distinct()
        max_vist_news = Post.objects.published().annotate(
        count=Count('hits')).order_by('-count').distinct()
        context['all_post'] = all_post
        context['new_post'] = new_post
        context['purpal_news'] = purpal_news
        context['max_vist_news'] = max_vist_news
        context['request'] = self.request
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
        end_news1 = Post.objects.published()[:1]
        end_news2 = Post.objects.published()[1:3]
        context['end_news1'] = end_news1
        context['end_news2'] = end_news2
        context['author'] = author
        return context


class TagPostList(ListView):
    paginate_by = 2
    template_name = 'blog/tag_post_list.html'
    def get_queryset(self):
        global hashtag
        tag_id = self.kwargs.get('tag_id')
        tag_slug = self.kwargs.get('tag_slug')
        title = self.kwargs.get('title')
        hashtag = get_object_or_404(Hashtag, slug=tag_slug, id=tag_id, title=title)
        ip = self.request.user.ip_address
        if ip not in hashtag.hits.all():
            hashtag.hits.add(ip)
            hashtag.save()
        return hashtag.post.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        end_news1 = Post.objects.published()[:1]
        end_news2 = Post.objects.published()[1:3]
        context['end_news1'] = end_news1
        context['end_news2'] = end_news2
        context['hashtag'] = hashtag
        return context

def like(request, id):
    user = request.user
    if not user.is_authenticated:
        return redirect('login_user')
    post = Post.objects.get(id=id)
    if user in post.like_user.all():
        post.like_user.remove(user)
    else:
        post.like_user.add(user)
    return redirect('blog:detail', post.slug, post.id)

class TagList(ListView):
    template_name = 'blog/tag_list.html'
    model = Hashtag

    def get_context_data(self):
        context = super().get_context_data()
        hashtags = Hashtag.objects.all()
        context['hashtags_group'] = my_grouper(10, hashtags)
        return context


