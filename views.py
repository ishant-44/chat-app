from django.shortcuts import render

def room(request, room_name):
    return render(request, 'chat/chat.html', {
        'room_name': room_name  # Pass the room name to the template
    })
def chat_home(request):
    return render(request, 'chat/chat.html')