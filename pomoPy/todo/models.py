from django.db import models
from django.contrib.auth.models import User 

class TodoModel(models.Model):
    author = models.ForeignKey(User,default=User.objects.first().pk, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    due_date = models.DateTimeField(blank=True, auto_now_add=False)
