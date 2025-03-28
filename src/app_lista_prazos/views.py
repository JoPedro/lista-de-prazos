from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic.list import ListView
from app_lista_prazos.models import Prazo


# Create your views here.
def index(request):
    return render(request, "index.html")


class PrazoListView(ListView):
    model = Prazo
