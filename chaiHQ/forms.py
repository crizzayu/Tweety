from django import forms
from .models import Tweet
# we create forms ==> to associate and use , the input feild given with existing models and django models
# we can create our own forms by passing data in veiws 
# But here we want to use django 

from django.contrib.auth.forms import UserCreationForm
# import user creation form
from django.contrib.auth.models import User
#import user model


class TweetForm(forms.ModelForm):
    class Meta:                    #syntax hai bnana hi pdega 
        model = Tweet
        fields = ['text' , 'photo'] #here we created array 

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

#make a view for registration of user -->go to views
