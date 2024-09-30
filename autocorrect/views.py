from django.shortcuts import render
import pandas as pd
import textdistance
import re
from collections import Counter

# Load the data for autocorrect when the server starts
words = []
with open('/Users/vipul/Desktop/Django/NLP/autocorrect/data/book.txt', 'r', encoding='utf8') as f:
    file_name_data = f.read().lower()

words = re.findall(r'\w+', file_name_data)
word_freq = Counter(words)
v = list(word_freq.keys())

def autocorrect(input_word):
    input_word = input_word.lower()
    if input_word in v:
        return f"Word is already there: {input_word}", None
    else:
        similarities = [1 - textdistance.Jaccard(qval=2).distance(w, input_word) for w in v]
        df = pd.DataFrame(list(zip(v, similarities)), columns=['Word', 'Similarity'])
        output = df.sort_values(['Similarity', 'Word'], ascending=[False, True]).head(10)
        return None, output.to_html(index=False, classes='table')

def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        error_message, corrected_suggestions = autocorrect(user_input)
        return render(request, 'autocorrect/index.html', {
            'user_input': user_input,
            'error_message': error_message,
            'corrected_suggestions': corrected_suggestions,
        })
    return render(request, 'autocorrect/index.html')
