from django.shortcuts import render


from .models import Article, ArticleImage, Comment


def articles(request):
    articles_list = Article.objects.all()
    data = {'articles': articles_list}
    return render(request, 'articles.html', data)


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    data = {'article': article}
    if request.method == "POST":
        user_data = request.POST
        Comment.objects.create(
            creator=request.user,
            article=article,
            body=user_data['body'],
        )
    return render(request, 'article_detail.html', data)


def create_article(request):
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
    return render(request, 'create_article.html', data)

