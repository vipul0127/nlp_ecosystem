from django.shortcuts import render
from pysentimiento import create_analyzer

# Create analyzers for emotion detection
emotion_analyzer = create_analyzer(task='emotion', lang='en')

# Dictionary to map emotions to emojis
emotion_to_emoji = {
    'joy': '😊',
    'sadness': '😔',
    'anger': '😠',
    'fear': '😨',
    'surprise': '😲',
    'disgust': '🤢',
    'others': '😐'
}

def emotion_d(text):
    result = emotion_analyzer.predict(text)
    # Return the emotion name and emoji
    emotion_name = result.output
    return emotion_name, emotion_to_emoji.get(emotion_name, '😐')

def index(request):
    detected_emotion_name = None
    detected_emotion_emoji = None

    if request.method == 'POST':
        user_input = request.POST.get('text')
        detected_emotion_name, detected_emotion_emoji = emotion_d(user_input)

    return render(request, 'emotion_detection/index.html', {
        'detected_emotion_name': detected_emotion_name,
        'detected_emotion_emoji': detected_emotion_emoji,
    })
