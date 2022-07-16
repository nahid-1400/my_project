from django.urls import path

from django.contrib.auth import views
from .views import ArticleView, ArticleCreate, ArticleUpdate, ArticleDelete

app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),

]

urlpatterns += [
    path('', ArticleView.as_view(), name='home'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
    path('article/update/<pk>', ArticleUpdate.as_view(), name='article-update'),
    path('article/delete/<pk>', ArticleDelete.as_view(), name='article-delete'),
]