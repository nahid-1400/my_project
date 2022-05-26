from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from blog.models import Post
from .mixins import FieldMixins, FormValidMixin


class ArticleView(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FieldMixins, FormValidMixin, CreateView):
    template_name = 'registration/article-create-update.html'
    model = Post

