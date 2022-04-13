from django.urls import path
from blog.views import home_view, DetailClass, ArticleCateGoryList, CateGoryList

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home'),
    path('post/<slug>-<id>', DetailClass.as_view(), name='detail'),
    path('category/<slug>', ArticleCateGoryList.as_view(), name='article-category'),
    path('category/<slug>/page/<int:page>', ArticleCateGoryList.as_view(), name='article-category'),
    path('category/', CateGoryList.as_view(), name='category'),
    path('category/page/<int:page>', CateGoryList.as_view(), name='category'),

]