from django.contrib import admin
from django.contrib.auth.hashers import make_password

# Register your models here.

from .models.admins import Admins
from .models.customers import Customers
from .models.devices import Devices
from .models.users import Users

class adminAdmins(admin.ModelAdmin):
    list_display = ('noAdmin', 'namaAdmin', 'emailAdmin', 'nomorHpAdmin', 'alamatAdmin')

    def save_model(self, request, obj, form, change):
        super().save_model(self, obj, form, change)

        user, created = Users.objects.get_or_create(username=obj.noAdmin, defaults={
            'password' : make_password('default_password'),
            'role': Users.ADMIN
        })

        if not created:
            user.role = Users.ADMIN
            user.save()

admin.site.register(Admins, adminAdmins)

admin.site.register(Customers)
admin.site.register(Devices)
admin.site.register(Users)