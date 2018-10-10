from django.db import models



class Musical(models.Model):
     songName = models.CharField(max_length=100)
     album = models.CharField(max_length=100)
     artist = models.CharField(max_length=100)
     duration = models.IntegerField()
     rating = models.IntegerField()
     pub_date = models.DateTimeField('date published')

def __str__(self):
    return self.songName
