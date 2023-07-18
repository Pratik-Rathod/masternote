from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class NotesModel(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)   
    # is_draft = models.BooleanField()
    