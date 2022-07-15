from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
# Create your models here.

TIPOS_CATEGORAIA = (
    ('TERROR', 'Terror'),
    ('SUSPENSE','Supense'),
    ('ANIMACAO', 'Animação'),
    ('ACAO', 'Ação'),
    ('OUTROS', 'Outros'),
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=4000)
    categoria = models.CharField(max_length=20, choices=TIPOS_CATEGORAIA)
    vizualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to='thumb_filmes')

    def __str__(self):
        return self.titulo