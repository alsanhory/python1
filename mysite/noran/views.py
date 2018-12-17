from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def yahya(request):
    return HttpResponse("hello bakor and yahya")
def mohaned(request):
    return render(request,'moh.html')
