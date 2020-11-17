from django.db import models
from django.conf import settings
from django.db.models import Model 
import uuid

class Sobre(models.Model):
    id_sobre = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo_pb = models.ImageField(upload_to = 'images', default = ' ')
    logo_br = models.ImageField(upload_to = 'images', default = ' ')
    descricao = models.TextField()
    foto = models.ImageField(upload_to = 'images')

class EventoAgendado(models.Model):
    id_evento = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_inicial = models.DateField()
    data_final = models.DateField(null=True, blank=True)
    titulo = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    link = models.URLField(max_length=200, default = ' ')

class Perfil(models.Model):
    id_perfil = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=200)
    profissao = models.CharField(max_length=200)
    linkedin = models.URLField(max_length=200, null=True, blank=True) 
    site = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    biografia = models.TextField()
    foto = models.ImageField(upload_to = 'images')

class Atividade(models.Model):
    id_atividade = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_ministrante = models.CharField(max_length=200)
    nome_atividade = models.CharField(max_length=200)
    descricao_atividade = models.TextField()
    foto_ministrante = models.ImageField(upload_to = 'images')
    link = models.URLField(max_length=200, null=True, blank=True)
    PALESTRA = 'PALESTRA'
    MINICURSO = 'MINICURSO'
    TIPO_ATIVIDADE = [
        (PALESTRA, 'PALESTRA'),
        (MINICURSO, 'MINICURSO'),
    ]
    tipo_atividade = models.CharField(max_length=200, choices=TIPO_ATIVIDADE,default=PALESTRA,)

class Evento(models.Model):
    id_evento = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(default = ' ')
    atividades = models.ManyToManyField(Atividade)