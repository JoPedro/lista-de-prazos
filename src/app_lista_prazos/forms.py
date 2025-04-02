from django.forms import ModelForm

from app_lista_prazos.models import Prazo


class PrazoForm(ModelForm):
    class Meta:
        model = Prazo
        fields = "__all__"
