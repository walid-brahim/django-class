from django.db import models
from django.utils import timezone

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length = 50)
    dscription = models.TextField(max_length=200)
    time = models.DateTimeField(auto_now=True)
    time = models.DateTimeField(timezone.now)
