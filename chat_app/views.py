from django.shortcuts import render
from queue import Queue

rus_speakers = Queue()
span_speakers = Queue()
eng_speakers = Queue()
germ_speakers = Queue()

# Create your views here.
def index(request):
    return render(request, "chat_app/index.html")

def chat(request):
    know_languages = request.POST["know-languages"]
    learning_languages = request.POST["learning-languages"]
    room_name = request.POST["room_name"]
    return render(request, "chat_app/chat.html", {
        "know_lang": know_languages,
        "learning_lang": learning_languages,
        "room_name": room_name
    })