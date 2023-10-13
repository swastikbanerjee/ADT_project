from django.db import models

# Create your models here.
class Assignment(models.Model):
  name = models.CharField(max_length=255)
  content = models.FileField(upload_to='students/', max_length=254)

# class Report(models.Model):
#   studname = models.CharField(upload_to = 'teachers/', max_length=255)