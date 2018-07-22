from django.db import models

# Create your models here.

class Notification(models.Model):
    frm = models.CharField(max_length=50)
    to = models.CharField(max_length=50)
    ticket_no = models.IntegerField()
    txid = models.CharField(max_length=500)
    stream = models.CharField(max_length=50)
    key = models.CharField(max_length=100)
