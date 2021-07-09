from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# request 안에 모든 전달 데이터가 들어있다.
def Hello_World(request):
    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!'})
