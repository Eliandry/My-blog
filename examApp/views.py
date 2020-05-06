from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import auth
from .forms import UserRegistrationForm


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
            args = {}
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            args['form'] = 'Аккаунт успешно создан'
            return render(request, "login.html", args)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'form': user_form})


def validate(request):
    if request.GET:
        email = request.GET.get('email')
        is_taken = User.objects.filter(email=email).exists()
        if is_taken:
            data = {
                "is_taken": "Этот почтовый адрес уже занят!"
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'ok': 'все ок :) '})
