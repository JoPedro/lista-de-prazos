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

        atualizados = 0
        inseridos = 0

        for prazo in seed_data["data"]:
            data_de_início = datetime.strptime(
                prazo["data_de_início"], "%d/%m/%Y"
            ).replace(tzinfo=timezone.get_current_timezone())

            values = {
                "identificador": prazo["identificador"],
                "data_de_início": data_de_início,
                "prazo_1_em_dias": prazo["prazo_1_em_dias"],
                "prazo_2_em_dias": prazo["prazo_2_em_dias"],
            }

            try:
                prazo = Prazo.objects.get(identificador=values["identificador"])
                changed = False
                for key, value in values.items():
                    if getattr(prazo, key) != value:
                        changed = True
                        setattr(prazo, key, value)
                if changed:
                    prazo.save()
                    atualizados += 1
                    print(f'Prazo "{values["identificador"]}" atualizado')
            except Prazo.DoesNotExist:
                add_prazo = Prazo(**values)
                add_prazo.save()
                inseridos += 1
                print(f'Prazo "{values["identificador"]}" inserido')

        self.stdout.write(
            self.style.SUCCESS(
                f"{inseridos} prazos inseridos e {atualizados} atualizados com sucesso."
            )
        )
