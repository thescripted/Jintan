from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-Binary'),
        ('OT', 'Other'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)

class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
