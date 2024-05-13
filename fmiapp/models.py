from django.db import models

# Create your models here.
class FarmerInfo(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=12)
    aadharno=models.CharField(max_length=12,primary_key=True)
    regdate=models.CharField(max_length=30)

class MerchantInfo(models.Model):

    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    firmname=models.CharField(max_length=100)
    firmaddress=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    aadharno=models.CharField(max_length=12,primary_key=True)
    panno=models.CharField(max_length=10)
    gstno=models.CharField(max_length=15)
    regdate=models.CharField(max_length=30)

class LoginInfo(models.Model):
    userid=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=20)

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    feedbacktext=models.TextField()
    feedbackdate=models.CharField(max_length=30)