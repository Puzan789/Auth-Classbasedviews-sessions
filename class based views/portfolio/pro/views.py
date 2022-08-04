from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from requests import request
from .forms import contactform


def myview(request):
    return HttpResponse ('<h1>we are the champions </h1>')

class MYview(View):
    name='ram'
    def get(self,request):
        return HttpResponse(self.name)
# def vieww(request):
#     return render(request,'enroll/dj.html')
class vieww(View):
    def get(self,request):
        return render(request,'enroll/dj.html')

def vin(request):
    context={'msg':'hello fucking peoples wassup'}
    return render(request,'enroll/har.html',context)
class diesel(View):
    def get(self,request):
        context={'msg':'hello fuckerss you  peoples are at class based views '}
        return render(request,'enroll/har.html',context)
# def formm(request):
#     if request.method=='POST':
#         form=contactform(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#         return HttpResponse("hello guys your form has been submitted")
#     else:
#         form=contactform()
#         return render(request,'enroll/get.html',{'form':form})
class formm(View):
    def get(self,request):
        form=contactform()
        return render(request,'enroll/get.html',{'form':form})
    def post(self,request):
        if request.method=='POST':
            form=contactform(request.POST)
            if form.is_valid():
                print(form.cleaned_data['name'])
        return HttpResponse("hello guys your form has been submitted")
        

        
