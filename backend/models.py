from django.db import models
import uuid

# Create your models here.


class Player(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)


class UserTab(models.Model): #inheritance from models.Model
    userid = models.CharField(max_length=60, null=False, blank=False, unique=True)
    useremail = models.CharField(max_length=200, default='username@example.com')
    password = models.CharField(max_length=200)
    userloginhost = models.CharField(max_length=200, default='example.com')
    totalscore = models.IntegerField( default=0 )
    last_login_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    login_token = models.CharField(max_length=255, unique=True, editable=False, null=True, blank=True)

    class Meta:
        ordering = ['-totalscore'] 
        '''from doc, sort table output by totalscore descending'''
   
    def save(self, *args, **kwargs):
        if not self.login_token:
            self.login_token = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        return self.userid 