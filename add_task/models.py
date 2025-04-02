from django.db import models

# Create your models here.
class TodoItem(models.Model):
  title = models.CharField(max_length=256)
  details = models.TextField()
  createdOn = models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  
