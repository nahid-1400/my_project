from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,

)
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post
from .forms import ProfileForm
from .mixins import (
    FieldMixins,
    FormValidMixin,
    AuthorAccessArticleMixin,
    ArticleDeleteMixin,
    AuthorSuperUsersAccessMixin,
    LoginMixin
)
from .models import User
from django.urls import reverse_lazy


from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import redirect

class ArticleView(LoginRequiredMixin, AuthorSuperUsersAccessMixin, ListView):
    template_name = 'registration/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(author=self.request.user)


class ArticleCreate(AuthorSuperUsersAccessMixin, FieldMixins, FormValidMixin, LoginRequiredMixin, CreateView):
    template_name = 'registration/article-create-update.html'
    model = Post

class ArticleUpdate(AuthorSuperUsersAccessMixin, AuthorAccessArticleMixin, FieldMixins, FormValidMixin,LoginRequiredMixin, UpdateView):
    template_name = 'registration/article-create-update.html'
    model = Post

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')
    template_name = 'registration/profile.html'

    def get_object(self, *args, **kwargs):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class ArticleDelete(AuthorSuperUsersAccessMixin, ArticleDeleteMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('account:home')
    template_name = 'registration/author_confirm_delete.html'

class Login(LoginMixin, LoginView):
    pass

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'فعال سازی حساب کاربری شما.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('ایمیلی حاوی لینک فعال سازی برای شما ارسال شد')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('blog:home')
    else:
        return HttpResponse('لینک منقضی شده است')