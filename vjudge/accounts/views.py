from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
import datetime
from django.utils.timezone import utc
from contests.models import *
import requests


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                print(user)
                b = Profile(uname = user)
                b.save()
                return redirect('login')

        context = {'form': form}
        return render(request , 'front/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request , 'front/login.html', context)

@login_required(login_url = '/loginPage/')
def logoutUser(request):
    logout(request)
    return redirect('login')

#@login_required(login_url = '/loginPage/')
def home(request):

    #Profile.objects.all().delete()
    #contests = Contest.objects.all()
    #total_contests = contests.count()
    usertype = request.user.username
    print(usertype)
    context = {
         'usertype': usertype
    }
    return render(request , 'front/home.html',context)

def aboutpage(request):
    return render(request, 'front/about.html')

def profile(request):

    usr = request.user.username
    print(usr)
    pro = Profile.objects.get(uname = usr )
    print(request.user.username)



    return render(request, 'front/profile.html',{'pro':pro})

def mysubmission(request):

    sub = Submission.objects.filter(user = request.user.username).order_by('-pk')
    return render(request, 'front/mysubmission.html',{'sub':sub})
