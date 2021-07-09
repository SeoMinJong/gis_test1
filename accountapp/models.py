from django.db import models

# Create your models here.

# 장고에서 제공해주는 기본 모델(models.Model)을 상속을 받아 와준다.
class NewModel(models.Model):
    text = models.CharField(max_length=255, null=False) # 최대 문자열 길이(max_length, null을 허용하지 않음(null=False)
