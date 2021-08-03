from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articleapp.forms import ArticleCreateForm
from articleapp.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    success_url = reverse_lazy('accountapp:Hello_World')  # reverse_lazy = class에서 주소를 불러올 때 사용되는 함수
    template_name = 'articleapp/create.html'  # 불러와줄 html 파일을 가져와서 주소로 들어갔을 때 해당 페이지를 불러온다.

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(self, form)
