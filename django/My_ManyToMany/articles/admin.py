from django.contrib import admin
from .models import Article, Comment # 명시적 상대경로 표현

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
