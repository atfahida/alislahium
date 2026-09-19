from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=50
    )

    classes = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name



class Event(models.Model):

    EVENT_TYPES = [
        ("Individual", "Individual"),
        ("Group", "Group"),
    ]

    event_name = models.CharField(
        max_length=100
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    event_type = models.CharField(
        max_length=20,
        choices=EVENT_TYPES
    )

    stage = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.event_name
