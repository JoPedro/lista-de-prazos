from django.urls import path

from . import views

urlpatterns = [
    path("", views.PrazoListView.as_view(), name="prazo-list"),
]
