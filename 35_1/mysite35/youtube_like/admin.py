from django.contrib import admin
from .models import User, Chanel, Like, Comment, User, Video

# Register your models here.
admin.site.register(User)
admin.site.register(Chanel)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Video)
