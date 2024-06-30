from django.contrib import admin
from .models import Post,Comment

class CommentInline(admin.TabularInline): # new
    model = Comment
class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
    CommentInline,
    ]


admin.site.register(Post,ArticleAdmin)
admin.site.register(Comment)
