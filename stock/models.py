# models.py serve para definir a estrutura dos dados que a aplicação manipula e fornece uma interface para interagir com a base de dados de forma eficiente e organizada.
from django.db import models

cidades_opcoes = [
    ("Faro", "Faro"),
    ("Quarteira", "Quarteira"),
    ("Lagos", "Lagos"),
    ("Lagoa", "Lagoa"),
    ("Portimão", "Portimão"),
    ("Albufeira", "Albufeira"),
    ("Sagres", "Sagres"),
    ("Aljez", "Aljez"),
    ("Via Real de Santo António", "Via Real de Santo António"),
    ("Olhão", "Olhão"),
    ("Aljezur", "Aljezur"),
    ("S. Teotónio", "S. Teotónio"),
    ("Aljez", "Aljez"),
    ("Ferreiras", "Ferreiras"),
    ("Vidigueira", "Vidigueira"),
    ("Barreiro", "Barreiro"),
    ("Lisboa", "Lisboa"),
    ("Estremoz", "Estremoz"),
    ("Oeiras", "Oeiras"),
    ("Alges", "Alges"),
    ("Elvas", "Elvas"),
    ("Amadora", "Amadora"),
    ("Correia", "Correia"),
    ("Carregado", "Carregado"),
    ("Portalegre", "Portalegre"),
    ("Santarém", "Santanrém"),
    ("Castelo Branco", "Castelo Branco"),
    ("Fundão", "Fundão"),
    ("Coimbra", "Coimbra"),
    ("Covilhã", "Covilhã"),
    ("Catanhede", "Catanhede"),
    ("Soito", "Soito"),
    ("Guarda", "Guarda"),
    ("Viseu", "Viseu"),
    ("Figueira de Castelo Rodrigo", "Figueira de Castelo Rodrigo"),
    ("Porto", "Porto"),
    ("Amarante", "Amarante"),
    ("Esposende", "Esposende"),
    ("Vila do Conde", "Vila do Conde")
]

class Artigo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    localizacao = models.CharField(max_length=100, choices=cidades_opcoes)  
    quantidade = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.nome
