from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from playbox2.models.admins import Admins

class Customers(models.Model):
    noCust = models.PositiveIntegerField(unique= True, validators=[
        MinValueValidator(1),
        MaxValueValidator(10**4-1)
    ])

    namaCust = models.CharField(max_length=255)
    emailCust = models.CharField(max_length=255, unique=True)
    nomorHpCust = models.CharField(max_length=13, unique=True)
    pesanCust = models.CharField(max_length=255)
    alamatCust = models.CharField(max_length=255)
    tanggalSewa = models.DateField()
    admin = models.ForeignKey(Admins, on_delete=models.CASCADE)

    def __str__(self):
        return self.namaCust