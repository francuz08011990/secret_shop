from django.contrib import admin

from .models import *


class ArticleImageAdmin(admin.TabularInline):
    model = ArticleImage


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageAdmin]
    list_display = ('id', 'creator', 'title')
    search_fields = ('title', )
    list_filter = ('creator', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass



