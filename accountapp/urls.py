from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import Hello_World, AccountCreateView, AccountDetailView

app_name = 'accountapp'

urlpatterns = [ # 어떤 패턴으로 라우팅을 해줄수 있는지를 입력해주는 곳
    path('Hello_World/', Hello_World, name='Hello_World'), # 경로지정('홈페이지의 경로/', 실제 파일 내부의 함수 이름, name='지정할 이름')

    path('Login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'), # django에서 제공하는 LoginView를 사용해서 로그인

    path('Logout/', LogoutView.as_view(), name='logout'),

    path('Create/', AccountCreateView.as_view(), name='create'), # class이기 때문에 바로 사용할 수 없고 as_view로 함수를 뱉어줘야한다.

    path('detail/<int:pk>',AccountDetailView.as_view(), name='detail'),
    # DetailVeiw같은 경우 특정 user 객체의 Key값을 받아야 해당하는 객체의 detailView를 볼 수 있기 때문에 <int:tk>로 key를 넘겨준다. tk:Primarykey
]