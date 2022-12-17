from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Medic(models.Model):
    name = models.CharField(max_length=50)
    room = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f"{self.name} | {self.room}"

