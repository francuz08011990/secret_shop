from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    creator = models.ForeignKey(User, verbose_name='Создатель')
    title = models.CharField('Заголовок', max_length=150)
    body = models.TextField('Статья', max_length=4000)

    class Meta:
        abstract = False
        unique_together = ['creator', 'title']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name='Изображение статьи')
    image = models.ImageField(
        'Фото статьи',
        upload_to='user_uploads/article_images/',
        blank=True,
        null=True
    )

    class Meta:
        abstract = False
        verbose_name = 'Избражение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.image.name.split('/')[-1]


class Comment(models.Model):
    creator = models.ForeignKey(User, verbose_name='Комментатор')
    article = models.ForeignKey(Article, verbose_name='Статья')
    body = models.TextField('Комментарий', max_length=500)

    class Meta:
        abstract = False
        verbose_name = 'Комментатор'
        verbose_name_plural = 'Комментаторы'

    def __str__(self):
        return self.body[:50]
