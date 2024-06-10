from django.db import models

class ChatMessage(models.Model):
    user_id = models.CharField(max_length=255)
    query = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}: {self.query}"
