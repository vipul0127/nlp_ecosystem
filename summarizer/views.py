from django.shortcuts import render
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

# Load the small English NLP model from SpaCy
nlp = spacy.load('en_core_web_sm')


def summarize_text(text, num_sent=3):
    doc = nlp(text)

    # Remove stopwords and punctuation
    token1 = []
    stopwords = list(STOP_WORDS)
    allowed_pos = ['NOUN', 'PROPN', 'VERB', 'ADJ']
    for token in doc:
        if token.text in stopwords or token.text in punctuation:
            continue
        if token.pos_ in allowed_pos:
            token1.append(token.text)

    # Calculate word frequencies
    word_freq = Counter(token1)
    max_frq = max(word_freq.values())

    for word in word_freq:
        word_freq[word] = word_freq[word] / max_frq

    # Calculate sentence scores
    sent_token = [sent.text for sent in doc.sents]
    sent_score = {}
    for sent in sent_token:
        for word in sent.split():
            if word.lower() in word_freq:
                if sent not in sent_score:
                    sent_score[sent] = word_freq[word.lower()]
                else:
                    sent_score[sent] += word_freq[word.lower()]

    # Get the summary
    summary = nlargest(num_sent, sent_score, key=sent_score.get)
    return " ".join(summary)


def summarizer_view(request):
    summary = None
    original_text = None

    if request.method == 'POST':
        text = request.POST.get('text')
        num_sentences=int(request.POST.get('num_sentences', 3))
        if(num_sentences%2!=0):
            num_sentences = int(num_sentences/2)+1
        else:
            num_sentences = int(num_sentences/2)
        # Default to 3 sentences if not provided
        summary = summarize_text(text, num_sentences)
        original_text = text

    return render(request, 'summarizer/index.html', {
        'summary': summary,
        'original_text': original_text
    })