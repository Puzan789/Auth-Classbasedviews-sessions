from django.contrib import messages
from django.shortcuts import render
from .forms import signupform
from django.contrib.auth.forms import AuthenticationForm
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
    fm=AuthenticationForm()
    return render(request,'auths/login.html',{'form':fm})
