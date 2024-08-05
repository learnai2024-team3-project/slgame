from django.db import models

# Create your models here.

class Player(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)