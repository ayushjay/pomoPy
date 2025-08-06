from django.db import models

class TodoM(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=200)