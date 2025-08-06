from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    due_date = models.DateTimeField(blank=True, auto_now_add=False)
