from django.http import Http404
from django.shortcuts import get_object_or_404
from blog.models import Post
from django.shortcuts import redirect

class FieldMixins():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['title', 'slug', 'description', 'image',  'published_time', 'is_special', 'status', 'category']
        if self.request.user.is_superuser:
            self.fields.append('author')
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            if not self.obj.status == 'i':
                self.obj.status = 'd'
        return super().form_valid(form)

class AuthorAccessArticleMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Post, pk=pk)
        if article.author == request.user and article.status in ['b', 'd'] or request.user.is_superuser:
            return super().dispatch(request, pk, *args, **kwargs)
        else:
            raise Http404('شما اجازه دسترسی به این صفحه را ندارید.')

class AuthorSuperUsersAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_author or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('account:profile')


class ArticleDeleteMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('شما اجازه حذف مقالات را ندارید.')

class LoginMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return redirect('account:home')
            else:
                return redirect('account:profile')
        return super().dispatch(request, *args, **kwargs)
