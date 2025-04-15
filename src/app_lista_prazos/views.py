from datetime import datetime, timedelta
from django.shortcuts import render
from django.views.generic.list import ListView
from app_lista_prazos.forms import PrazoForm
from app_lista_prazos.models import Prazo
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request, "prazo_list.html")


def form_adicionar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        prazo_em_dias = int(request.POST.get("prazo_em_dias"))

        data_de_vencimento = request.POST.get(
            "data_de_vencimento"
        ) or timezone.now().replace(
            tzinfo=timezone.get_current_timezone(), hour=0, minute=0, second=0
        ) + timedelta(
            days=prazo_em_dias
        )

        if type(data_de_vencimento) == str:
            data_de_vencimento = datetime.strptime(
                data_de_vencimento, "%d/%m/%Y"
            ).replace(tzinfo=timezone.get_current_timezone())

        add_prazo = Prazo(id, prazo_em_dias, data_de_vencimento)
        add_prazo.save()

    form = PrazoForm()
    context = {"form": form}
    return render(request, "app_lista_prazos/form.html", context)


class PrazoListView(ListView):
    model = Prazo
    # Terminar paginação
    # paginate_by = 20

    ordering = ["id"]
