from django.contrib import messages
from django.core.paginator import Paginator
from datetime import datetime, timedelta
from django.db import IntegrityError
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from app_lista_prazos.forms import PrazoForm
from app_lista_prazos.models import Prazo
from django.utils import timezone


def index(request):
    # Lista paginada
    prazo_list = Prazo.objects.all().order_by("data_de_início")
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
    identificador = request.POST.get("identificador").strip()
    prazo = Prazo.objects.filter(identificador=identificador)

    if len(prazo) > 0:
        messages.error(
            request,
            "Cadastro inválido. Há um prazo com o mesmo identificador.",
        )
        return HttpResponseRedirect("/")

    data_de_início = datetime.strptime(
        request.POST.get("data_de_início"), "%Y-%m-%d"
    ).replace(tzinfo=timezone.get_current_timezone())
    prazo_1_em_dias = int(request.POST.get("prazo_1_em_dias"))
    prazo_2_em_dias = int(request.POST.get("prazo_2_em_dias"))

    values = {
        "identificador": identificador.strip(),
        "data_de_início": data_de_início,
        "prazo_1_em_dias": prazo_1_em_dias,
        "prazo_2_em_dias": prazo_2_em_dias,
    }

    add_prazo = Prazo(**values)
    add_prazo.save()
    messages.success(request, "Prazo adicionado com sucesso.")

    return HttpResponseRedirect("/")


def excluir(request, pk):
    prazo = Prazo.objects.get(identificador=pk)

    if request.method == "POST":
        prazo.delete()
        messages.success(request, "Prazo removido com sucesso.")
        return HttpResponseRedirect("/")

    context = {"prazo": prazo}

    return render(request, "app_lista_prazos/excluir.html", context)
