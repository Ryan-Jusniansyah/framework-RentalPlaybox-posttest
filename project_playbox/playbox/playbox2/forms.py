from django import forms
from .models.devices import Devices

class DevicesForm(forms.ModelForm):
    class Meta:
        model = Devices
        fields = "__all__"