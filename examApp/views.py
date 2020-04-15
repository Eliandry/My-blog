from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from .forms import UserRegistrationForm


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