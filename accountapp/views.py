from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# request 안에 모든 전달 데이터가 들어있다.
from accountapp.models import NewModel


def Hello_World(request):
    if request.method == "POST":

        temp = request.POST.get('input_text') # input_text라는 이름의 값을 가져와준다.

        model_instance = NewModel()  # 데이터베이스에 접근하기 위해 모델을 불러와 준다.
        model_instance.text = temp   # 데이터베이스에 만들어뒀던 text변수에 넘겨준다.
        model_instance.save()        # 실제로 데이터베이스에 해당

        return render(request, 'accountapp/hello_world.html', context={'model_instance': model_instance})
        # 받아온 텍스트를 넘겨줘서 출력할 수 있도록 한다.
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!'})
