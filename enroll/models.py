from django.db import models

# Create your models here.
class User(models.Model):
    token_number = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    section_sem = models.CharField(max_length=70)