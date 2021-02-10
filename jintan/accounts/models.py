from django.db import models
class UserProfile(models.Model):

    owner = models.ForeignKey('user.Auth', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    favorite_card = models.ForeignKey("models.Card", on_delete=models.CASCADE)


class Card(models.Model):

    class Quality(models.IntegerChoices):
        POOR = 1
        FAIR = 2
        DECENT = 3
        GREAT = 4
        AMAZING = 5

    owner = models.ForeignKey('user.Auth', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    quality = models.IntegerField(choices=Quality.choices)
    autographed = models.BooleanField(default=False)
    selling = models.BooleanField(default=False)  # card in auction/"buy now"
