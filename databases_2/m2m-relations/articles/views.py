from django.views.generic import ListView
from .models import Article, Category, Compilation


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'



