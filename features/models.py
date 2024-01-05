from django.db import models


# Create your models here.
class InboxDetails(models.Model):
    uid = models.CharField(max_length=100)
    from_id = models.CharField(max_length=200)
    subject = models.CharField(max_length=254)
    content = models.TextField(max_length=10000)

class SentDetails(models.Model):
    uid = models.CharField(max_length=100)
    to_id = models.CharField(max_length=200)
    subject = models.CharField(max_length=254)
    content = models.TextField(max_length=10000)

class BinDetails(models.Model):
    uid = models.CharField(max_length=100)
    from_id = models.CharField(max_length=200)
    subject = models.CharField(max_length=254)
    content = models.TextField(max_length=10000)

class JunkDetails(models.Model):
    uid = models.CharField(max_length=100)
    from_id = models.CharField(max_length=200)
    subject = models.CharField(max_length=254)
    content = models.TextField(max_length=10000)