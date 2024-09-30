from django.urls import path
from .views import index
app_name='sentiment_analysis'
urlpatterns = [
    path('', index, name='index'),
]
