# from django.db import models
# from django.utils import timezone
#
# # Create your models here.
#
#
# class Like(models.Model):
#     # time = models.DateTimeField(auto_now_add=True)
#     quantity = models.PositiveIntegerField(null=True, blank=False)
#     # author = models.CharField(max_length=60)
#
#
# class User(models.Model):
#     name = models.CharField(max_length=60)
#     email = models.EmailField(max_length=254)
#     status = models.BooleanField()
#     rating = models.IntegerField(null=True, blank=False)
#     avatar = models.FileField()
#
#
# class Article(models.Model):
#     name = models.CharField(max_length=100)
#     text = models.TextField(null=True, blank=True)
#     time = models.DateTimeField(default=timezone.now)
#     rating = models.ForeignKey(Like, on_delete=models.CASCADE, null=True, blank=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#
#
# class Comment(models.Model):
#     text = models.TextField(null=True, blank=True)
#     time = models.DateTimeField(auto_now_add=True)
#     author = models.CharField(max_length=60)

#
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.utils.translation import gettext as _
#
# GENRE_CHOICES = (
#     (1, _("Not selected")),
#     (2, _("Comedy")),
#     (3, _("Action")),
#     (4, _("Beauty")),
#     (5, _("Other"))
# )
#
#
# class Author(models.Model):
#     pseudonym = models.CharField(max_length=120, blank=True, null=True)
#     name = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.name
#
#
# class Article(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
#     text = models.TextField(max_length=10000, null=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
#     genre = models.IntegerField(choices=GENRE_CHOICES, default=1)
#
#     def __str__(self):
#         return "Author - {}, genre - {}, id - {}".format(self.author.name, self.genre, self.id)
#
#
# class Comment(models.Model):
#     text = models.CharField(max_length=1000)
#     article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
#     comment = models.ForeignKey('myapp36.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
#                                 related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return "{} by {}".format(self.text, self.user.username)
#
#
# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return "By user {} to article {}".format(self.user.username, self.article.id)
#
#
#

