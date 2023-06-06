from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_string(request):
    return HttpResponse('THIS MY FIRST APPLICATION1')
def app1_htmlpage(request):
    return render(request, 'htmlpage.html')

