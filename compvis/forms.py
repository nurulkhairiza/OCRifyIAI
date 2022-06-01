from django import forms
from .models import *

class OCRInputForm(forms.Form):
    input_img = forms.ImageField()

class TranslatorInputForm(forms.Form):
    source_language = forms.CharField(max_length=8)
    target_language = forms.CharField(max_length=8)
    text = forms.CharField()

class TTSInputForm(forms.Form):
    tts = forms.CharField()