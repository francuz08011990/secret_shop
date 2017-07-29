from django.shortcuts import render

from .models import Article


def articles(request):
    articles_list = Article.objects.all()
    template_name = 'articles.html'
    data = {'articles': articles_list}
    return render(request, template_name, data)


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    template_name = 'article_detail.html'
    data = {'article': article}
    return render(request, template_name, data)
