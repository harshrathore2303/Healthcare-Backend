from django.db import models
from django.conf import settings

class Doctor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=13, unique=True)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    profession = models.CharField(max_length=80)
    degree = models.CharField(max_length=80)

    def __str__(self):
        return self.name
