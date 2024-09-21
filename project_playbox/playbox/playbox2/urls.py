from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about),
    path("", views.homepage),
    path("rent/", views.rent),
]
