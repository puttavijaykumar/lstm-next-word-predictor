from django.shortcuts import render
from .utils import predict_next_word

def index(request):
    prediction = ""
    input_text = ""
    if request.method == "POST":
        input_text = request.POST.get("input_text")
        prediction = predict_next_word(input_text)
    return render(request, "predictor/index.html", {"prediction": prediction, "input_text": input_text})
