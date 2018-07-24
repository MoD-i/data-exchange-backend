from django.db import models

# Create your models here.

class Notification(models.Model):
    # nid = models.AutoField(primary_key=True)
    frm = models.CharField(max_length=50)
    to = models.CharField(max_length=50)
    ticket_no = models.IntegerField()
    txid = models.CharField(max_length=500)
    stream = models.CharField(max_length=50)
    key = models.CharField(max_length=100)
    read = models.BooleanField(default=False)

    def _str_(self):
        return f'Notification from {self.frm}. Ticket No. {ticket_no}. Trxn ID {txid}'

    class Meta:
        ordering = ('-id', )
