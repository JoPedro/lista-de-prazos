from django.forms import DateTimeInput, ModelForm

from app_lista_prazos.models import Prazo


class PrazoForm(ModelForm):
    class Meta:
        model = Prazo
        fields = "__all__"
        widgets = {"data_de_vencimento": DateTimeInput(format="%d/%m/%Y")}
