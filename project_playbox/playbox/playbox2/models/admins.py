from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Admins(models.Model):
    noAdmin = models.PositiveBigIntegerField(unique=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(10**4-1)
    ])

    namaAdmin = models.CharField(max_length=255)
    emailAdmin = models.CharField(max_length=255, unique=True)
    nomorHpAdmin = models.CharField(max_length=13, unique=True)
    alamatAdmin = models.CharField(max_length=255)

    def __str__(self):
        return self.namaAdmin