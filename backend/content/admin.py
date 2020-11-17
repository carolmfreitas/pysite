from django.contrib import admin
from .models import Sobre
from .models import Evento
from .models import Perfil
from .models import Atividade
from .models import EventoAgendado

class SobreAdmin(admin.ModelAdmin):
    list_display = ('id_sobre', 'descrição')

admin.site.register(Sobre)

class EventoAgendadoAdmin(admin.ModelAdmin):
    list_display = ('id_evento', 'titulo', 'data_inicial', 'local')

admin.site.register(EventoAgendado)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id_perfil', 'nome', 'city', 'profissao')

admin.site.register(Perfil)

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('id_atividade', 'nome_atividade', 'nome_ministrante', 'tipo_atividade')

admin.site.register(Atividade)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id_evento', 'nome')

admin.site.register(Evento)