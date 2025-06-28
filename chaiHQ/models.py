from django.db import models
#we are creating a model 
#import jango usme contrib -> auth -> models milega
from django.contrib.auth.models import User # this user is from admin panel (editable , configruble)
from cloudinary.models import CloudinaryField

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    photo = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):#when we integrate it in admin , we can able to modify the url given by this 
        return f'{self.user.username} - {self.text[:10]}'
