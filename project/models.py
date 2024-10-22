from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Theme(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="themes")

    title = models.CharField(max_length=256)

    description = models.TextField()

    def __str__(self):
        return self.title


class Message(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="messages")

    text = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.text} - {self.created_at}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    bio = models.CharField(max_length=200, null=True, blank=True)

    telegram = models.CharField(max_length=128, blank=True, null=True)
    instagram = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.user.username
