from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Post


class FieldMixins():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['author', 'title', 'slug', 'description', 'image',  'published_time', 'status' ,'category']

        elif request.user.is_author:
            self.fields = ['title', 'slug', 'description', 'image', 'published_time', 'category']
        else:
            raise Http404('شما اجازه افزودن پست را ندارید')
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)

class AuthorAccessArticleMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Post, pk=pk)
        if article.author == request.user and article.status == 'd' or request.user.is_superuser:
            return super().dispatch(request, pk, *args, **kwargs)
        else:
            raise Http404('شما اجازه ویرایش این صفحه را ندارید')

class ArticleDeleteMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('شما اجازه حذف مقالات را ندارید.')


