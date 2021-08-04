from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from articleapp.forms import ArticleCreateForm
from articleapp.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articleapp/create.html'  # 불러와줄 html 파일을 가져와서 주소로 들어갔을 때 해당 페이지를 불러온다.

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk' : self.object.pk})

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)
    # 해당 구문은 form_valid라는 함수(view에 정보를 넘겨주기 전에 마지막으로 거치는 과정)에 직접 writer 정보를 넘겨주는 것

class AritcleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'