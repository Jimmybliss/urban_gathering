from django.db import models

class Invitation(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    past_attendance = models.BooleanField()
    social_media_followers = models.IntegerField()
    interest_in_music = models.BooleanField()
    interest_in_art = models.BooleanField()
    interest_in_technology = models.BooleanField()
    distance_from_venue = models.FloatField()
    has_plus_one = models.BooleanField()
    invited = models.BooleanField(default=False)

    def __str__(self):
        return self.name
