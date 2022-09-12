from django.shortcuts import render
from transformers import GPT2LMHeadModel, GPT2Tokenizer
# Create your views here.
def blog(request):
    return render(request, 'index3.html')

def generatedblog(request):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
    model = GPT2LMHeadModel.from_pretrained("gpt2-large", pad_token_id=tokenizer.eos_token_id)
    sentence = request.GET.get('text3')
    input_ids = tokenizer.encode(sentence, return_tensors='pt')
    output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
    blog = print(tokenizer.decode(output[0], skip_special_tokens=True))
    return render(request, 'index3.html', {'blog': blog})

