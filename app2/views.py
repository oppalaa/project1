from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string(request):
    return HttpResponse('<marquee><h1>THIS IS MY SECOND APPLICATION</h1></marquee>')
def html(request):
    return render(request,'html.html')
