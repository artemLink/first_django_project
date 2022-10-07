from django.db import models


# Create your models here.

class users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class message(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    full_text = models.TextField()


class count(models.Model):
    count = models.IntegerField()
    user_from = models.IntegerField()
    user_to = models.IntegerField()