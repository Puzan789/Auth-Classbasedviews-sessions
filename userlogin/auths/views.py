
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect
from .forms import signupform,edituserprofile,editadminprofile
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
#user signup views
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
#userlogin views
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
#userprofile views
def userprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser == True:
                fm=editadminprofile(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                users=None
                fm=edituserprofile(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                print("saved")
        else:
            if request.user.is_superuser==True:
                users=User.objects.all()
                fm=editadminprofile(instance=request.user)
            else: 
                users=None
                fm=edituserprofile(instance=request.user)
        return render(request, 'auths/profile.html' ,{'name':request.user,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/login/')
#user logout views
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
# change password wih using old password
def changepass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user) #will redirect to your profile page
                print("saved")
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'auths/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
# change password without using old password
def changepass1(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                print("saved")
                return HttpResponseRedirect('/profile/')
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'auths/changepass1.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

