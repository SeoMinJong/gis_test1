from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )
    # OneToOneField 연결해주는 field / on_delete = User 객체가 삭제됐을 때 삭제를 할 것인가 models.CASCADE(종속 = 삭제 하겠다.)
    # on_delete = models.Set_NULL => 삭제를 시켜도 NULL로 남겨서 이 Profile은 남기겠다.
    # related_name = profile과 연결해주겠다.
    image = models.ImageField(upload_to='profile/', null=True)
    # upload_to = upload경로를 지정해주는 것, null = 해당 이미지를 넣지 않아도 된다는 의미
    nickname = models.CharField(max_length=11, unique=True)
    message = models.CharField(max_length=200, null=False)