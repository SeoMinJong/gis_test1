from django.contrib.auth.forms import UserCreationForm

class AccountCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 중요한 부분

        self.fields['username'].disabled=True

