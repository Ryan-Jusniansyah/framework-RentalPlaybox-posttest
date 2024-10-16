from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about),
    path("", views.homepage),
    path("rent/", views.rent),
    path("device/", views.device_index, name='device_index'),
    path('device/create/', views.device_create, name='device_create'),
    path("device/update/<int:device_id>", views.device_update, name="device_update"),
    path("device/delete/<int:device_id>", views.device_delete, name="device_delete")
]
