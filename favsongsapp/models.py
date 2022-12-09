from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Fav(models.Model):
    song_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    year_of_release = models.DateField()
    rating = models.IntegerField(blank=False, null=False)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=False, null=False)


    def __str__(self):
        return self.song_title
    

class Opinion(models.Model):
    song = models.ForeignKey(Fav, on_delete=models.SET_DEFAULT, default=1, blank=False, null=False)
    opinion = models.TextField(max_length=500, blank=False, null=False)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return str(self.reviewer) 