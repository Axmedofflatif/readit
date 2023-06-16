from django.db import models

from profiles.models import Profile


class Feedback(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}'s feedback"
