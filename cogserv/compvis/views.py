from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from PIL import Image
from .forms import *
from .ocr import *
from .text_to_speech import *
from .translator import *

context = {
    'result': '',
    'available_languages': available_languages,
    'source_language': 'en',
    'target_language': 'id',
    'selected_source': 'en',
    'selected_target': 'id'
}

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'image_form.html', context)

def ocr_post(request):
    if request.method == 'POST':
        form = OCRInputForm(request.POST, request.FILES)
        if form.is_valid():
            ocr_result = sendOCR(Image.open(request.FILES['input_img']))
            context['result'] = ocr_result
        return render(request, 'image_form.html', context)

def translate_post(request):
    if request.method == 'POST':
        form = TranslatorInputForm(request.POST, request.FILES)
        if form.is_valid():
            translation_result = translate(request.POST['text'], request.POST['source_language'], request.POST['target_language'])
            context['result'] = translation_result
            context['selected_source'] = request.POST['source_language']
            context['selected_target'] = request.POST['target_language']
        return redirect(reverse('index'))

def tts_post(request):
    if request.method == 'POST':
        form = TTSInputForm(request.POST, request.FILES)
        if form.is_valid():
            text_to_speech(request.POST['tts'])
        return redirect(reverse('index'))