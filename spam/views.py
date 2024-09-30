import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import spacy
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Preprocess function remains unchanged
def preprocess(text):
    doc = nlp(text)
    lemalist = [token.lemma_ for token in doc]
    lemmatized_text = ' '.join(lemalist)
    nostoplist = [token.text for token in nlp(lemmatized_text) if not token.is_stop and not token.is_punct]
    return ' '.join(nostoplist)

# Load your dataset for training
data = pd.read_csv('/Users/vipul/Desktop/Django/NLP/spam/data/data.csv')  # Update the path based on your project structure
x_train = data['sms']  # Change here to reflect the new column name
y_train = data['label']

# Define the model (should be trained beforehand)
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('RF', RandomForestClassifier())
])

# Train the model with the dataset
model.fit(x_train, y_train)

# View to handle form submission
def classify_message(request):
    if request.method == "POST":
        message = request.POST.get('message')
        if message:
            processed_message = preprocess(message)
            prediction = model.predict([processed_message])[0]
            result = 'Spam' if prediction == 1 else 'Not Spam'
            return render(request, '/Users/vipul/Desktop/Django/NLP/spam/templates/spam_detection/result.html', {'result': result, 'message': message})

    return render(request, '/Users/vipul/Desktop/Django/NLP/spam/templates/upload.html')

# View to handle CSV upload and classification
def classify_csv(request):
    if request.method == "POST" and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        path = default_storage.save('tmp/messages.csv', csv_file)
        df = pd.read_csv(path)
        df['processed'] = df['sms'].apply(preprocess)  # Change here to reflect the new column name
        df['prediction'] = model.predict(df['processed'])
        df['result'] = df['prediction'].apply(lambda x: 'Spam' if x == 1 else 'Not Spam')

        # Return the dataframe as an HTML table for simplicity
        result_html = df[['sms', 'result']].to_html()  # Change here to reflect the new column name
        return HttpResponse(result_html)

    return render(request, 'upload_csv.html')
