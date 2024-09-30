# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Route to the main app index
    path('emotion/', include('emotion_detection.urls')),  # Route to the emotion detection app
    path('summarizer/', include('summarizer.urls')),      # Route to the summarizer app
    path('autocorrect/', include('autocorrect.urls')),    # Route to the autocorrect app
   
    path('spam/', include('spam.urls')),   
    path('sentiment_analysis/', include('sentiment_analysis.urls')),     # Route to the sentiment analysis app
]
