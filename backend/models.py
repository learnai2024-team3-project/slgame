from django.db import models

# Create your models here.

class Player(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

class UserTab(models.Model): #inheritance from models.Model
    userid = models.CharField(max_length=60, null=False, blank=False, unique=True)
    useremail = models.CharField(max_length=200, default='username@example.com')
    userloginhost = models.CharField(max_length=200, default='example.com')
    totalscore = models.IntegerField( default=0 )
    acctimes = models.IntegerField( default=0 )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['-totalscore'] 
        '''from doc, sort table output by totalscore descending'''
   
    def __str__(self):
        return self.userid 