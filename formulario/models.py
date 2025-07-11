from django.db import models

class Quiz(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

from django.db import models

class Pergunta(models.Model):
       TIPOS = (
           ('multipla', 'Escolha múltipla'),
           ('texto', 'Resposta texto'),
           ('curta', 'Resposta curta'),
       )
       quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='perguntas')
       texto = models.CharField(max_length=255)
       tipo = models.CharField(max_length=20, choices=TIPOS)
       resposta_correta = models.CharField(max_length=255, null=True, blank=True)  # Campo adicionado
       def __str__(self):
           return self.texto


class OpcaoResposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='opcoes')
    texto_opcao = models.CharField(max_length=200)
    is_correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto_opcao
