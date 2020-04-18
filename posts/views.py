from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from .forms import AddArticle, AddNews
import datetime


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
        form = AddNews(request.POST, request.FILES)
        model_news = form.save(commit=False)
        model_news.name = request.POST.get('name')
        model_news.text = request.POST.get('text')
        model_news.time = now.strftime("%Y-%m-%d %H:%M")
        model_news.image = request.FILES.get('image')
        model_news.save()
        return HttpResponseRedirect('/')
    return render(request, 'createNews.html', {'form': form, 'username': auth.get_user(request).username})
