from django.db import models
from django.conf import settings

class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patients")
    name = models.CharField(max_length=80)
    dob = models.DateField()
    problem = models.TextField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
