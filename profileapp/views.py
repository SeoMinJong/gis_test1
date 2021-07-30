from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_reqired
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:Hello_World')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):  # form = 클라이언트에게 요청을 받아 입력받은 데이터 (image, nickname, )
        form.instance.user = self.request.user
        # form은 Profile안에 있는 form만을 가져오는 것이기 때문에 user가 존재하지 않는다 고로 그 form을 가지고있는 instance객체를 접근해서 가져와야하고
        # request 즉, 요청을 받은 user의 아이디를 넣어주는 것이다.
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})


@method_decorator(profile_ownership_reqired, 'get')
@method_decorator(profile_ownership_reqired, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    # success_url = reverse_lazy('accountapp:Hello_World')
    # detail페이지로 넘어가고 싶으나 pk가 필요하기 때문에 불가능하다.
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={ 'pk' : self.object.user.pk})
