
#views defines the functionlity 
#and we add this views in jinja templates
# Create your views here.
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import render
from .forms import UserRegistrationForm

#we need a "get" bcz django puts a ors layer through which we can interact with database
# and we have some shortcut given by sjango 
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')#here render index.html

#to list all tweets
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets':tweets})




#create tweets

#cases:
# we give user an empty form 
#
#1. form given to user(we give user a form and a request is returned form that form and we are handling it ) -> handle it
#2. we are giving user an empty form
#3. we get forms with data from user -->> just render it

@login_required

def tweet_create(request): # if user give us a filled form 
    if request.method == "POST": #check if req is a post?
        form = TweetForm(request.POST, request.FILES) # we get req and .files help us to get access the files also

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user # to get user from request bcz form dont have user 
                                      # and we want user 
            tweet.save()
            
            return redirect('tweet_list')
    else:
        form = TweetForm() #if we give an empty fprm to user
    return render(request, 'tweet_form.html', {'form':form})




# edit tweets
@login_required

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user= request.user)       #for editng,we need a data(tweet) from model ,
                                                                            #in tweet look at tweet_id as primary key(pk)  
                                                                            # AND AND only user who request the edit can edit users data NOT everyones
    if request.method == "POST": #check if req is a post?
        form = TweetForm(request.POST, request.FILES, instance=tweet)   # we get req and .files help us to get access the files also BUT
                                                                        # but use instance to know that it is an old tweet which is editing
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    
    else:
        form = TweetForm(instance=tweet)  #instanece to get the tweet for editing
    return render(request, 'tweet_form.html', {'form':form})




#TWEET DELETE
@login_required

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    
    if(request.method == "POST"):
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html',{'tweet': tweet})


#User registration using form ---> go to forms.py

def register(request):
    if request.method == 'POST':
        
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
        
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html',{'form': form})
# this will not work bcz it is a django default link and it redirect to this ==>> /accounts/login ,,,,  Request URL:	http://127.0.0.1:8000/accounts/login/?next=/chaiHQ/create/
#and after login it will lead to chaiHQ/create
# so we have to define the where URL is coming in django 
# go to ==>> { settings.py } and redefine where is redirecting goes to manually 


#searching 

from django.db.models import Q


def tweet_search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Tweet.objects.filter(
            Q(text__icontains = query) | Q(user__username__icontains = query)
        
        ).order_by('-created_at')

    return render(request, 'tweet_search.html',
            {'query': query,
             'results': results
            }
    )