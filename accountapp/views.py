from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Hello_World(request):
    return render((request, 'accountapp/hello_world.html'))