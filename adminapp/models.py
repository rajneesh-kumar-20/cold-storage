from django.db import models

# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    aadharno=models.CharField(max_length=12,primary_key=True)
    noofpacket=models.IntegerField()
    duration=models.IntegerField()
    rate=models.IntegerField()
    totalamt=models.IntegerField()
    advance=models.IntegerField()
    restamt=models.IntegerField()
    bookingdate=models.CharField(max_length=30)


class News(models.Model):
    newstext=models.TextField()
    newsdate=models.CharField(max_length=30)
