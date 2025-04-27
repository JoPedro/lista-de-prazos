from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="prazo_list"),
]
