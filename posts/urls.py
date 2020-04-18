from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from django.views.generic import ListView
from django.conf.urls.static import static
from .models import News, Article
urlpatterns = [
    path('create/article/', views.new),
    path('create/news/', views.new_news),
    path('allnews/', ListView.as_view(queryset=News.objects.all().order_by('-time')[:20],
                                      template_name='news.html')),
    path('allarticle/', ListView.as_view(queryset=Article.objects.all().order_by('-time')[:20],
                                         template_name='posts.html')),
    path('posts/<int:id>',views.getposts),
    path('news/<int:id>',views.getnews),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()