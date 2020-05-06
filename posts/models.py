from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    time = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/article/', blank=True)


class News(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='images/news/', blank=True)
    time = models.DateTimeField()

