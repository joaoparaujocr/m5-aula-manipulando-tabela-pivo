from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Medic(models.Model):
    name = models.CharField(max_length=50)
    room = models.CharField(max_length=2)
    patients = models.ManyToManyField(
        Patient, through="Schedule", related_name="medics"
    )

    def __str__(self) -> str:
        return f"{self.name} | {self.room}"

class Schedule(models.Model):
    medic = models.ForeignKey(
        "Medic",
        on_delete=models.CASCADE,
    )
    patient = models.ForeignKey(
        "Patient",
        on_delete=models.CASCADE
    )
    description = models.TextField()