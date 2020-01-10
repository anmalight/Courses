from django.contrib import admin
from .models import Article, Like, Comment, Author


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Author)