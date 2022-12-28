from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string1(request):
    return HttpResponse('This is String1')

def string2(request):
    return HttpResponse('This is String2')