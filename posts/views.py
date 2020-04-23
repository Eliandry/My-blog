from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from .forms import AddArticle, AddNews
from .models import Article,News
import datetime

def index(request):
    article_all=Article.objects.all()
    news_all = News.objects.all()

    article_list = [i for i in article_all]
    news_list = [i for i in news_all]
    article_post=article_list[-4:]
    news_post = news_list[-4:]
    main_post= article_list[-1]
    return render(request, 'index.html', {'username': auth.get_user(request).username,'post_article':article_post,
                                          'post_news':news_post,'main_post':main_post})


def new(request):
    form = AddArticle()
    now = datetime.datetime.now()
    if request.method == "POST":
        form = AddArticle(request.POST, request.FILES)
        model_article = form.save(commit=False)
        model_article.name = request.POST.get('name')
        model_article.time = now.strftime("%Y-%m-%d %H:%M")
        model_article.description = request.POST.get('description')
        model_article.text = request.POST.get('text')
        model_article.save()
        return HttpResponseRedirect('/')
    return render(request, 'createArticle.html', {'form': form, 'username': auth.get_user(request).username})


def new_news(request):
    form = AddArticle()
    now = datetime.datetime.now()
    if request.method == "POST":
        fort = AddNews(request.POST, request.FILES)
        if fort.is_valid():
            model_news = fort.save(commit=False)
            model_news.name = request.POST.get('name')
            model_news.text = request.POST.get('text')
            model_news.time = now.strftime("%Y-%m-%d %H:%M")
            model_news.image = request.FILES.get('image')
            model_news.save()
            return HttpResponseRedirect('/')
    return render(request, 'createNews.html', {'form': form, 'username': auth.get_user(request).username})


def getposts(request, id):
    sub = Article.objects.get(id=id)
    return render(request, 'onepost.html', {'form': sub,'username': auth.get_user(request).username})
def getnews(request, id):
    sub = News.objects.get(id=id)
    return render(request, 'onepost.html', {'form': sub, 'username': auth.get_user(request).username})
