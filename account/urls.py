from django.urls import path
from .views import (
    ArticleView,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete,
    Profile,
    signup,
    activate
)
app_name = 'account'

urlpatterns = [
    path('', ArticleView.as_view(), name='home'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
    path('article/update/<pk>', ArticleUpdate.as_view(), name='article-update'),
    path('profile', Profile.as_view(), name='profile'),
    path('article/delete/<pk>', ArticleDelete.as_view(), name='article-delete'),
    path('signup/', signup, name='signup'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',activate, name='activate'),
]