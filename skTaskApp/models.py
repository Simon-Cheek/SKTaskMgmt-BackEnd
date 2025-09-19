from django.db import models

# Create your models here.
class Task(models.Model):

    # Define Task Related Enums
    class Priority(models.TextChoices):
        P1 = "P1"
        P2 = "P2"
        P3 = "P3"
    class Status(models.TextChoices):
        ACTIVE = "Active"
        COMPLETE = "Complete"
        EXPIRED = "Expired"


    # Auto Added id field
    name = models.CharField(max_length=250)
    description = models.TextField()
    assignedTo = models.CharField(max_length = 100)
    priority = models.CharField(max_length=5, choices=Priority.choices, default=Priority.P3)
    assignedDate = models.DateTimeField()
    dueDate = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
