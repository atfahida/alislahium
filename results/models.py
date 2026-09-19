from django.db import models

# Create your models here.
from django.db import models
from participants.models import Participant


class Result(models.Model):

    PLACE_POINTS = {
        "1": 10,
        "2": 8,
        "3": 5,
    }

    GRADE_POINTS = {
        "A": 10,
        "B": 5,
        "C": 3,
    }

    participant = models.OneToOneField(
        Participant,
        on_delete=models.CASCADE
    )

    place = models.CharField(
        max_length=1,
        choices=[
            ("1", "First"),
            ("2", "Second"),
            ("3", "Third"),
        ]
    )

    grade = models.CharField(
        max_length=1,
        choices=[
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
        ]
    )

    place_points = models.IntegerField(
        default=0
    )

    grade_points = models.IntegerField(
        default=0
    )

    total_points = models.IntegerField(
        default=0
    )

    def save(self, *args, **kwargs):

        self.place_points = self.PLACE_POINTS.get(
            self.place,
            0
        )

        self.grade_points = self.GRADE_POINTS.get(
            self.grade,
            0
        )

        self.total_points = (
            self.place_points +
            self.grade_points
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.participant.student.name