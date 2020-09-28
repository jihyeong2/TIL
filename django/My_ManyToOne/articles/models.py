from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='articles')
    title=models.CharField(max_length=50)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comments')
    content=models.CharField(max_length=200)
    create_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)