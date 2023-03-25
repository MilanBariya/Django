from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Eat no junck food for entire month!")

def february(resuest):
    return HttpResponse("Walk for atleast 20 minutes every day!")