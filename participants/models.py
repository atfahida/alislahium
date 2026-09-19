from django.db import models

# Create your models here.
from django.db import models
from students.models import Student
from events.models import Event


class Participant(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    bib_number = models.CharField(
        max_length=20
    )

    registered_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.student.name} - "
            f"{self.event.event_name}"
        )