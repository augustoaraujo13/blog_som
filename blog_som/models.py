from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    create_data = models.DateField(auto_now_add=True)

