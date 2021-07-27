from django.urls import path, include

from profileapp.views import ProfileCreateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create')
    # 메인앱에서 분기를 했기 때문에 profileapp/create로 들어가지기 때문에 나눠진다.
]