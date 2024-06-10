from django.shortcuts import render
from django.http import JsonResponse
import requests
from .models import ChatMessage

def chat_view(request):
    if request.method == "POST":
        user_query = request.POST.get("query")
        user_id = request.session.session_key
        response = requests.post('https://api.gemini.com/v1/chat', data={'query': user_query}, headers={'Authorization': 'AIzaSyCcQ3eiR0gI8nPOMak6OhOYJAC8UT_e524'})
        response_data = response.json()

        ChatMessage.objects.create(user_id=user_id, query=user_query, response=response_data['response'])

        chat_history = ChatMessage.objects.filter(user_id=user_id).order_by('-timestamp')[:3]

        return JsonResponse({'chat_history': list(chat_history.values())})
    
    return render(request, 'chats/chat.html')

