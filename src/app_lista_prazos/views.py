from django.shortcuts import render
from django.views.generic.list import ListView
from app_lista_prazos.forms import PrazoForm
from app_lista_prazos.models import Prazo


# Create your views here.
def index(request):
    return render(request, "prazo_list.html")


def form_adicionar(request):
    if request.method == "POST":
        add_prazo = Prazo(id=request.POST["id"], prazo=int(request.POST["prazo"]))
        add_prazo.save()

    form = PrazoForm()
    context = {"form": form}
    return render(request, "app_lista_prazos/form.html", context)


class PrazoListView(ListView):
    model = Prazo
