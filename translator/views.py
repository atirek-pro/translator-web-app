from django.shortcuts import render
from googletrans import Translator
# Create your views here.
def translate(request):
    return render(request, 'index.html')

def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text:', text, 'lang:', lang)

    translator = Translator()
    dt = translator.detect(text)
    dt2 = dt.lang
    translated =translator.translate(text, lang)
    tr = translated.text
    return render(request, 'index.html', {'translated': tr, 'u_lang': dt2, 't_lang': lang})