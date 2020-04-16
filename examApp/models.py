from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=70)
    time = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField()



class News(models.Model):
    name = models.CharField(max_length=60)
    text = models.TextField()
    image = models.ImageField()
    time = models.DateTimeField()
