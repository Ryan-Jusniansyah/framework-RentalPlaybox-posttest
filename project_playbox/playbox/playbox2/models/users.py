from django.db import models

class Users(models.Model):
    CUSTOMER = 1
    DEVICE = 2
    ADMIN = 3

    ROLE_CHOICES = (
        (CUSTOMER, "Customer"),
        (DEVICE, "Device"),
        (ADMIN, "Admin")
    )

    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.IntegerField(choices=ROLE_CHOICES)

    def __str__(self):
        return self.username