from django.db import models
from datetime import timezone
# Create your models here.

class StudentAccount(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=timezone)

    def __str__(self):
        return self.name
