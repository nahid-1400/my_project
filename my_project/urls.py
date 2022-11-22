"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import login_users, logout_user
from .views import header_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('login/', login_users, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('header/', header_view, name='header'),
    path('account/', include('account.urls')),
    path('comment/', include('comment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

