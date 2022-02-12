from django.urls import path
from blog.views import home_view, DetailClass, CateGoryList

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home'),
    path('post/<slug>-<id>', DetailClass.as_view(), name='detail'),
    path('category/<slug>', CateGoryList.as_view(), name='category'),
    path('category/<slug>/page/<int:page>', CateGoryList.as_view(), name='category'),

]