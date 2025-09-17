from django.db import models

# Create your models here.
class Task(models.Model):
    # Auto Added id field
    name = models.CharField(max_length=250)
    description = models.TextField()
    assignedTo = models.CharField(max_length = 100)
    priority = models.CharField(max_length=5)
    assignedDate = models.DateTimeField()
    dueDate = models.DateTimeField()
    status = models.CharField(max_length=20)
