from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sree(request):
    return HttpResponse('this is my second string response')
def chinnu(request):
    return render(request,'chinnu.html')
