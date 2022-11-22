from django.urls import path
from blog.views import \
    (home_view
, DetailClass,
     ArticleCateGoryList,
     CateGoryList,
     AuthorList,
    ArticlePreview,
    Search,
     like,
    TagPostList,
    about_us,
    TagList,
    AllPost,
     )

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home'),

    path('article/<slug>-<id>', DetailClass.as_view(), name='detail'),
    path('preview/<slug>-<pk>', ArticlePreview.as_view(), name='preview'),
    path('category/<slug>', ArticleCateGoryList.as_view(), name='article-category'),
    path('category/<slug>/page/<int:page>', ArticleCateGoryList.as_view(), name='article-category'),
    path('search', Search.as_view(), name='search'),
    path('search/page/<int:page>', Search.as_view(), name='search'),
    path('category/', CateGoryList.as_view(), name='category'),
    path('category/page/<int:page>', CateGoryList.as_view(), name='category'),
    path('author/<slug:username>', AuthorList.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name='author'),
    path('hashtag/<tag_slug>/<tag_id>/<title>', TagPostList.as_view(), name='hashtag'),
    path('hashtag/<tag_slug>/<tag_id>/page/<int:page>/<title>', TagPostList.as_view(), name='hashtag'),
    path('hashtag/', TagList.as_view(), name='hashtag-list'),
    path('like/<id>', like, name='like'),
    path('about_us', about_us, name='about-us'),
    path('articles', AllPost.as_view(), name='all-article'),

]