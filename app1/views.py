from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jaya(request):
    return HttpResponse('this is my string response')
def manu(request):
    return render(request,'manu.html')
