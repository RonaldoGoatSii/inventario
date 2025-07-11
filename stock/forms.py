from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['nome', 'descricao', 'localizacao', 'quantidade']
        labels = {
            'nome': 'Nome do Artigo',
            'descricao': 'Descrição',
            'localizacao': 'Localização',
            'quantidade': 'Quantidade',
        }
