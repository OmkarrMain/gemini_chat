from django.urls import path
from .views import chat_view

urlpatterns = [
    path('chatt/', chat_view, name='chat'),
]
