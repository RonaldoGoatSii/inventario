from django import forms
from .models import Quiz, Pergunta

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do Quiz'
            }),
        }

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['tipo']
        widgets = {
            'texto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Texto da pergunta'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
