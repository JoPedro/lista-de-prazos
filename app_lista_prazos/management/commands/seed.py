import json
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from app_lista_prazos.models import Prazo


class Command(BaseCommand):
    help = "Comando para popular a base de dados com dados simulados"

    def handle(self, *args, **options):
        with open("./app_lista_prazos/management/commands/json/data.json", "r") as file:
            seed_data = json.load(file)

        for prazo in seed_data["data"]:
            identificador = prazo["identificador"]
            prazo_1_em_dias = prazo["prazo_1_em_dias"]
            prazo_2_em_dias = prazo["prazo_2_em_dias"]
            data_de_início = datetime.strptime(
                prazo["data_de_início"], "%d/%m/%Y"
            ).replace(tzinfo=timezone.get_current_timezone())

            data_de_vencimento_1 = data_de_início + timedelta(days=prazo_1_em_dias)
            data_de_vencimento_2 = data_de_início + timedelta(days=prazo_2_em_dias)

            Prazo.objects.update_or_create(
                identificador=identificador,
                data_de_início=data_de_início,
                prazo_1_em_dias=prazo_1_em_dias,
                prazo_2_em_dias=prazo_2_em_dias,
                data_de_vencimento_1=data_de_vencimento_1,
                data_de_vencimento_2=data_de_vencimento_2,
            )

            print(f'Prazo "{identificador}" inserido ou atualizado')

        self.stdout.write(
            self.style.SUCCESS(
                f'{len(seed_data["data"])} prazos inseridos ou atualizados com sucesso.'
            )
        )
