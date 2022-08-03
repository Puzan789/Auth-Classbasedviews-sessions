from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
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
