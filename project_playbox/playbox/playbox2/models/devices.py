from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from playbox2.models.admins import Admins

class Devices(models.Model):
    noDevice = models.PositiveBigIntegerField(unique=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(10**4-1)
    ])

    namaDevice = models.CharField(max_length=255)
    fasilitas = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255, unique=True)
    harga = models.PositiveBigIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10**10-1)
    ])
    admin = models.ForeignKey(Admins, on_delete=models.CASCADE)

    def __str__(self):
        return self.namaDevice