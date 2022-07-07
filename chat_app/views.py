from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "chat_app/index.html")

def chat(request, room_name):
    know_languages = request.POST["know-languages"]
    learning_languages = request.POST["learning-languages"]
    return render(request, "chat_app/chat.html", {
        "know_lang": know_languages,
        "learning_lang": learning_languages,
        "room_name": room_name
    })