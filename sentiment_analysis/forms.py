from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class SentenceForm(forms.Form):
    sentence = forms.CharField(max_length=500)
