from distutils.command.upload import upload
from pyexpat import model
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

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    ep_num = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo