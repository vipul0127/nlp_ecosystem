from django.urls import path
from .views import home
app_name = 'autocorrect'  # Set the app namespace
urlpatterns = [
    path('', home, name='home'),
]
