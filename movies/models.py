from django.db import models

# Create your models here.


class Genres(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title: models.CharField(max_length=255)
    release_year: models.DateField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
