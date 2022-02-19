from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_login(request):
    
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Succesfully logged in')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Password or username doesnt match')
    else:
        form=LoginForm()
    return render(request, 'account/login.html', {'form':form})

@login_required(login_url='login/')
def home(request):
    return render(request, 'account/home.html')


def user_registration(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user':new_user})
    else:
        form=RegistrationForm()
    return render(request, 'account/register.html', {'form':form})
