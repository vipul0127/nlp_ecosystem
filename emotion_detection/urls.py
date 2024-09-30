from django.urls import path
from . import views

app_name = 'emotion_detection'  # Set the app namespace

urlpatterns = [
    path('', views.index, name='index'),  # Define your index view
]
