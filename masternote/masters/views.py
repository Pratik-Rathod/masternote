from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, user_logged_in
from django.contrib import messages
from .forms import NewUsersForm
from django.forms import ValidationError
# Create your views here.


def home(request):
    return render(request, 'index.html')


def user_login(request):
    context = dict()
    if request.user.is_authenticated:
        return redirect('home')

    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Successful welcome back!")
                return redirect('home')
            else:
                messages.error(request, "Username or password was wrong")
                return redirect('login')
        else:
            context['login'] = AuthenticationForm()
    except Exception as e:
        print(e)
        messages.error(request, "Something wernt from ourside")
        return redirect('login')

    return render(request, 'masters/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, "See ya soon!")
    return redirect('home')


def user_register(request):
    context = dict()

    if request.user.is_authenticated:
        return redirect('home')

    try:
        if request.method == 'POST':
            form = NewUsersForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(
                    request, "Welcome to party! feel free to post content")
                newUser = authenticate(username=form.cleaned_data.get(
                    'username'), password=form.cleaned_data.get('password1'))
                login(request, newUser)
                return redirect('login') 
        else:
            form = NewUsersForm()

    except Exception as e:
        print(e)
        messages.error("something went wrong from ourside !")
    context['register_form'] = form
    return render(request, 'masters/register.html', context)
