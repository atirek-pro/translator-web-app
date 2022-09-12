from django.shortcuts import render
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
# Create your views here.
def getQA(request):
    return render(request, 'index2.html')

def comprehension(request):
    context =  request.GET.get('text')
    question =  request.GET.get('text2')
    nlp = pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')
    question_set = {
        'question': question,
        'context': context
    }
    results = nlp(question_set)
    answer = results['answer']
    return render(request, 'index2.html', {'answer': answer})
