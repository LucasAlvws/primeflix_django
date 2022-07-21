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

TEMPORADAS = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
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

    @property
    def get_temp(self):
        t = 0
        lista = []
        for ep in self.episodios.all():
            lista.append(ep.temporada)
        for i in lista:
            if i > t:
                t = i
        t = range(t)
        return t    

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    ep_num = models.IntegerField(default=0)
    temporada = models.IntegerField(default=0, choices=TEMPORADAS)

    def __str__(self):
        return self.titulo
    
    