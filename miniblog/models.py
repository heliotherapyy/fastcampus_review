from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add= True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('Post')

    def __str__(self):
        return self.content


class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    category = models.ForeignKey(Category, null=False, blank=True)
    tags = models.ForeignKey('Tag', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


