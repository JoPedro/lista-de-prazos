from django.core.paginator import Paginator
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_lista_prazos.forms import PrazoForm
from app_lista_prazos.models import Prazo
from django.utils import timezone


def index(request):
    # Lista paginada
    prazo_list = Prazo.objects.all().order_by("data_de_vencimento")
    paginator = Paginator(prazo_list, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Formulário
    form = PrazoForm()

    return render(
        request,
        "app_lista_prazos/index.html",
        {"page_obj": page_obj, "form": form},
    )


def adicionar(request):
    id = request.POST.get("identificador")
    prazo_em_dias = int(request.POST.get("prazo_em_dias"))

    data_de_vencimento = request.POST.get(
        "data_de_vencimento"
    ) or timezone.now().replace(
        tzinfo=timezone.get_current_timezone(), hour=0, minute=0, second=0
    ) + timedelta(
        days=prazo_em_dias
    )

    if type(data_de_vencimento) == str:
        data_de_vencimento = datetime.strptime(data_de_vencimento, "%d/%m/%Y").replace(
            tzinfo=timezone.get_current_timezone()
        )

    add_prazo = Prazo(id, prazo_em_dias, data_de_vencimento)
    add_prazo.save()

    return HttpResponseRedirect("/")


def excluir(request, pk):
    if request.method == "POST":
        return HttpResponseRedirect("/")

    prazo = Prazo.objects.get(identificador=pk)
    context = {"prazo": prazo}

    return render(request, "app_lista_prazos/excluir.html", context)
