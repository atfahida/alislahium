
from django.db import models


class Student(models.Model):

    student_id = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    class_name = models.CharField(
        max_length=20
    )

    division = models.CharField(
        max_length=10,
        blank=True
    )

    house = models.CharField(
        max_length=50
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    def __str__(self):
        return f"{self.student_id} - {self.name}"