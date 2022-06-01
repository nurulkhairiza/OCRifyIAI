from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ocr', views.ocr_post),
    path('translate', views.translate_post),
    path('tts', views.tts_post)
]