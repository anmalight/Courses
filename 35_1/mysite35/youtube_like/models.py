from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    age = models.PositiveIntegerField()


class Chanel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    viewers = models.PositiveIntegerField()

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=False)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)


class Video(models.Model):
    name = models.CharField(max_length=120)
    year_of_public = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
