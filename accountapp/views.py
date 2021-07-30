from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.

# request 안에 모든 전달 데이터가 들어있다.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreateForm
from accountapp.models import NewModel


@login_required
def Hello_World(request):
    # 현재
    if request.method == "POST":

        temp = request.POST.get('input_text')  # input_text라는 이름의 값을 가져와준다.

        model_instance = NewModel()  # 데이터베이스에 접근하기 위해 모델을 불러와 준다.
        model_instance.text = temp  # 데이터베이스에 만들어뒀던 text변수에 넘겨준다.
        model_instance.save()  # 실제로 데이터베이스에 저장해주는 것

        return HttpResponseRedirect(reverse('accountapp:Hello_World'))
        # 해당하는 app안에 있는 app_name으로 app의 위치를 알려주고 그 안에 있는 라우팅을 가져온다.
        # 다만 이때 HttpResponseRedirect 안에 인자는 주소가 들어가야 하기 때문에 reverse로 주소를 불러온다.
    else:
        data_list = NewModel.objects.all()  # NewModel이라는 데이터베이스에 있는 데이터들을 다 가져오는 법

        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})


class AccountCreateView(CreateView):
    model = User  # User를 만드는 것
    form_class = UserCreationForm  # User의 정보
    success_url = reverse_lazy('accountapp:Hello_World')  # reverse_lazy = class에서 주소를 불러올 때 사용되는 함수
    template_name = 'accountapp/create.html'  # 불러와줄 html 파일을 가져와서 주소로 들어갔을 때 해당 페이지를 불러온다.


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


has_ownership = [login_required, account_ownership_required]


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreateForm  # 새로운 값을 만들어 주는 역할
    context_object_name = 'target_user'  # 만들어진 객체에 접근하기 위한 역할
    # success_url = reverse_lazy('accountapp:Hello_World')
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.pk})


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:Hello_World')
    template_name = 'accountapp/delete.html'
