from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class UserProfile(models.Model):

    class Gender(models.IntegerChoices):
        MALE = 1
        FEMALE = 2
        NONBINARY = 3
        OTHER = 4

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=True)  # May be redundant...
    last_name = models.CharField(max_length=120, blank=True)
    gender = models.IntegerField(choices=Gender.choices, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    profile_url = models.CharField(max_length=128, blank=True)  # URL To profile picture


# something to store secure-information (e.g., payments) ... yeah nevermind.
# Don't store credit card information (see PCI Compliance)
class SecuredUserProfile(models.Model):
    pass


class CardStore(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Card(models.Model):
    class Quality(models.IntegerChoices):  # Subject to change.
        POOR = 1
        FAIR = 2
        GOOD = 3
        GREAT = 4
        MINT = 5

    autograph = models.BooleanField(default=False)
    quality = models.IntegerField(choices=Quality.choices)
    card_name = models.CharField(max_length=128)


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
