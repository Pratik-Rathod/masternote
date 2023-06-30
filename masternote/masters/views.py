from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages

# Create your views here.
def home(request):
   return render(request,'index.html')


def userlogin(request):
   context = dict()

   if request.POST:
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      user  = authenticate(username=username,password=password)
      if user is not None:
         login(request,user)
         return redirect('home')
      else:
         messages.error(request, "~Username or password was wrong")
         return redirect('login')
   else:    
      context['login'] = AuthenticationForm()

   return render(request,'masters/login.html',context)