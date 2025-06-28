from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.tweet_list,         name = 'tweet_list'),#here we rander a veiw so go to veiws page
    path('create/', views.tweet_create, name = 'tweet_create'),

    path('<int:tweet_id>/edit/',   views.tweet_edit,   name = 'tweet_edit'), # SYNTAX OF URL in int <int:tweet_id>
    path('<int:tweet_id>/delete/', views.tweet_delete, name = 'tweet_delete'),
    path('register/', views.register, name = 'register'),
    path('search/', views.tweet_search, name='tweet_search'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    