from django.db import models


class Theme(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    title = models.CharField(max_length=256)

    description = models.TextField()

    def __str__(self):
        return self.title


class Message(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='messages')

    text = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.text} - {self.created_at}"
