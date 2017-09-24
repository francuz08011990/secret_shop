from io import BytesIO
from PIL import Image

from django.shortcuts import render
from django.core.files.base import ContentFile

from .models import Article, ArticleImage, Comment


def articles(request):
    articles_list = Article.objects.all()
    template_name = 'articles.html'
    data = {'articles': articles_list}
    return render(request, template_name, data)


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    template_name = 'article_detail.html'
    data = {'article': article}
    if request.method == "POST":
        user_data = request.POST
        Comment.objects.create(
            creator=request.user,
            article=article,
            body=user_data['body'],
        )
    return render(request, template_name, data)


def create_article(request):
    template_name = 'create_article.html'
    data = {}
    if request.method == "POST":
        user_data = request.POST
        files = request.FILES.getlist('image')
        try:
            article = Article.objects.create(
                creator=request.user,
                title=user_data['title'],
                body=user_data['body'],
            )
            for file in files:
                img = ArticleImage.objects.create(article=article)
                img.image.save(file.name, file)
                data['message'] = 'Вы успешно создали статью!'
        except:
            data['error'] = 'Статья с таким названием уже существует!'
    return render(request, template_name, data)

