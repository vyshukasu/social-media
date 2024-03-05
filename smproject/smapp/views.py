from django.shortcuts import render

from django.http import HttpResponse

def home(request):
     return HttpResponse('hi')

def index(request):
     return render( request,'index.html')
