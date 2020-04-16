from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from .forms import UserRegistrationForm
from .models import Article,News
import datetime


def index(request):
    return render(request, 'index.html', {'username': auth.get_user(request).username})


def login(request):
    args = {}
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'login.html', args)
    else:
        return render(request, "login.html", args)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            args={}
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            args['form']='Аккаунт успешно создан'
            return render(request, "login.html", args)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'form': user_form})
def new(request):
    now = datetime.datetime.now()
    if request.method=="POST":
        model_article = Article()
        model_article.name=request.POST.get('name')
        model_article.time = now.strftime("%Y-%m-%d %H:%M")
        model_article.description = request.POST.get('description')
        model_article.text = request.POST.get('text')
        model_article.image=request.POST.get('image')
        model_article.save()
        return HttpResponseRedirect('/')
    return render(request,'createArticle.html')
def new_news(request):
    now = datetime.datetime.now()
    if request.method=="POST":
        model_news = News()
        model_news.name=request.POST.get('name')
        model_news.text = request.POST.get('text')
        model_news.time = now.strftime("%Y-%m-%d %H:%M")
        model_news.image=request.POST.get('image')
        model_news.save()
        return HttpResponseRedirect('/')
    return render(request,'createNews.html')
