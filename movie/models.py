from django.db import models

from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/', blank=True)
    image = models.ImageField(upload_to='images/', blank=True)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

