import os
import re
import pandas as pd
import joblib
from django.shortcuts import render
from .forms import UploadFileForm, SentenceForm  # Create forms for file upload and sentence input

# Load the model and vectorizer
vectorizer = joblib.load('/Users/vipul/Desktop/Django/NLP/sentiment_analysis/data/cvtransform.pkl')
model = joblib.load('/Users/vipul/Desktop/Django/NLP/sentiment_analysis/data/model.pkl')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'tsv'}

def preprocess_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    tokens = text.split()
    # You can integrate stopwords removal and stemming here
    return ' '.join(tokens)

def index(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES['file']
                if file and allowed_file(file.name):
                    data = pd.read_csv(file, delimiter='\t')
                    # Your processing logic here...
                    # Render the results in the template
                    return render(request, 'sentiment_analysis/results.html', {'data': data})

        elif 'sentence' in request.POST:
            form = SentenceForm(request.POST)
            if form.is_valid():
                sentence = form.cleaned_data['sentence']
                cleaned_sentence = preprocess_text(sentence)
                X_new = vectorizer.transform([cleaned_sentence]).toarray()
                prediction = model.predict(X_new)[0]
                sentiment = 'Positive' if prediction == 1 else 'Negative'
                return render(request, 'sentiment_analysis/result.html', {'sentiment': sentiment})

    return render(request, 'sentiment_analysis/index.html', {'form': UploadFileForm(), 'sentence_form': SentenceForm()})
