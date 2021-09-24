from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='article/', null=True, blank=False)
    content = models.TextField(null=True)
    # 장문을 고려해야하는 상황에는 TextField를 사용해주는 편이다.

    created_at = models.DateField(auto_now_add=True, null=True)
    # db에서 데이터가 생성될 때 자동적으로 생성이 될 수 있게 해주는 방법 auto_now_add=True

    like = models.IntegerField(default=0)