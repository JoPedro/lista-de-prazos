from django.forms import DateTimeInput, ModelForm

from app_lista_prazos.models import Prazo


class PrazoForm(ModelForm):
    class Meta:
        model = Prazo
        fields = [
            "identificador",
            "data_de_início",
            "prazo_1_em_dias",
            "prazo_2_em_dias",
        ]
        widgets = {
            "data_de_início": DateTimeInput(format="%d/%m/%Y"),
        }
