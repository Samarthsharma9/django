from django.db import models
from django.contrib.auth.models import User

'''class Registration_table(models.Model):
  username = models.CharField(max_length=50)
  first_name= models.CharField(max_length=100)
  last_name = models.CharField(max_length=50)
  email_address = models.EmailField(max_length=50)
  password = models.CharField(max_length=50)
  #confirm_password = models.CharField(max_length=50)'''
  


class Architect_table(models.Model):
  name = models.CharField(max_length=50)
  Bio = models.TextField(max_length=100)
  experience = models.CharField(max_length=50)

class Contractor_table(models.Model):
  name = models.CharField(max_length=50)
  Bio = models.TextField(max_length=100)
  experience = models.CharField(max_length=50)
  fees = models.IntegerField()
  
class Interior_Designer_table(models.Model):
  name = models.CharField(max_length=50)
  Bio = models.TextField(max_length=100)
  experience = models.CharField(max_length=50)
  fees = models.IntegerField()