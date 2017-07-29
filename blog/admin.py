from django.contrib import admin

from .models import *


class ArticleImageAdmin(admin.TabularInline):
    model = ArticleImage


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageAdmin,]


class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
