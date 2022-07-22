
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect
from django.urls import is_valid_path
from .forms import signupform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
def signup(request):
    if request.method == "POST":
        fm=signupform(request.POST)
        if fm.is_valid():
            messages.success(request,'!!!!your account is created!!!!')
            fm.save()
        fm=signupform()
        print('done')
    else:
        fm=signupform()
        print("error")

    return render(request,'auths/signup.html',{'form':fm})

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"login succesfully!!!!")
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request,'auths/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
def userprofile(request):
    if request.user.is_authenticated:
        return render(request, 'auths/profile.html' ,{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

