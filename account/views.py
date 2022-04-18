from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from blog.models import Post

@login_required()
def home(request):
    return render(request, 'registration/home.html')


class ArticleView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    template_name = 'registration/home.html'