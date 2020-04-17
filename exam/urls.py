"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from examApp import views
from examApp.models import News, Article
from django.views.generic import ListView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('auth/login/', views.login),
    path('auth/logout/', views.logout),
    path('auth/register/', views.register),
    path('create/article/', views.new),
    path('create/news/', views.new_news),
    path('allnews/', ListView.as_view(queryset=News.objects.all().order_by('-time')[:20],
                                      template_name='posts.html')),
    path('allarticle/', ListView.as_view(queryset=Article.objects.all().order_by('-time')[:20],
                                         template_name='posts.html'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
