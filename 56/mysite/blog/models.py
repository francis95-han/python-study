from django.db import models

# Create your models here.
class BlogPaot(models.model):
    title = models.Charfield(max_length=150)
    body = models.TextField()
    timestamp = models.DataTimeField()
