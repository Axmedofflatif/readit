from django.db import models


class Cantact(models.Model):
    full_name = models.CharField(max_length=221)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=221)
    message = models.TextField()

    def __str__(self):
        return self.full_name
