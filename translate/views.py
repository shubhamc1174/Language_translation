import json

from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator


def index(request):
    return render(request, 'translate/index.html')


def translated(request):
    text = request.POST.get('work')
    text = text.strip()

    to2 = request.POST.get("to")

    translator = Translator()
    trans_text = translator.translate(text, dest=to2)

    context = {
        'otext': text.strip('"'),
        'text': trans_text.text.strip('"'),
        'to2': to2,
    }

    return render(request, 'translate/translated.html', context)


def speech(request):
    return render(request, "translate/speech.html")
