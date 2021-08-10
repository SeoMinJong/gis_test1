from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreateForm
from articleapp.models import Article


@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articleapp/create.html'  # 불러와줄 html 파일을 가져와서 주소로 들어갔을 때 해당 페이지를 불러온다.

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)
    # 해당 구문은 form_valid라는 함수(view에 정보를 넘겨주기 전에 마지막으로 거치는 과정)에 직접 writer 정보를 넘겨주는 것


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'post')
@method_decorator(article_ownership_required, 'get')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreateForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'post')
@method_decorator(article_ownership_required, 'get')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 2