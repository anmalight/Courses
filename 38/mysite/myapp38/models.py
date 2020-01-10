from datetime import timedelta

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.


GENDER_CHOICES = (
    (1, _("Female")),
    (2, _("Male"))
)

TYPE_CHOICES = (
    (1, _("badger")),
    (2, _("monkey")),
    (3, _("bear"))
)


class Animal(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    age = models.PositiveIntegerField()
    added_at = models.DateTimeField(default=timezone.now)


class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=120, blank=True, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    age = models.PositiveIntegerField()


class Ticket(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.DO_NOTHING)
    lim_age = models.PositiveIntegerField(default=16, validators=[MinValueValidator(16), MaxValueValidator(150)])
    # lim_date = models.DateTimeField(default=timezone.datetime.max)
    lim_date = models.DateTimeField(default=timezone.now, max_length=timezone.now() + timedelta(days=1))

    def save(self, **kwargs):
        if not self.pk:
            self.lim_date = timezone.now() + timedelta(days=1)
        super().save(**kwargs)


class Visit(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    visitor = models.ForeignKey(Visitor, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(default=timezone.now)
    # count = models.PositiveIntegerField(default=0)



