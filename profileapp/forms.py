from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:  # 이미지로 생각했을 때 이미지 자체가 아닌 외부적인 정보같은 느낌
        model = Profile
        fields = ['image', 'nickname', 'message']  # 유저한테서 어떤 결정을 받을 것인지
