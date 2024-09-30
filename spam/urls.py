
from django.urls import path
from . import views

urlpatterns = [
    path('classify-message/', views.classify_message, name='classify_message'),
    path('classify-csv/', views.classify_csv, name='classify_csv'),
]
