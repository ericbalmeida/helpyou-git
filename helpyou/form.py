from django.forms import ModelForm
from .models import Mensagens

class MensagemForm(ModelForm):
    class Meta:
        model = Mensagens
        fields = ['mensagem']