from django.shortcuts import render, Http404, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm


def login_user(request):
    print('request.user', request.user)
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            raise Http404('Username or password not provided!')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('/')


def register_user(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    return render(request, 'users/register.html', {
        'form': form,
    })
