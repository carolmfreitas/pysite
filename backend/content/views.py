from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import EventoAgendado, Perfil, Evento, Sobre
from .forms import PerfilForm


def base_view(request):
    return render(request, 'content/index.html', {})

def sobre_detalhe(request):
    sobre = get_object_or_404(Sobre)
    return render(request, 'content/sobre_detalhe.html', {'sobre': sobre})

def eventos_list(request):
    lista_eventos = EventoAgendado.objects.all().order_by('data_inicial')
    paginator = Paginator(lista_eventos, 2)
    page = request.GET.get('page')
    eventos = paginator.get_page(page)
    return render(request, 'content/eventos_list.html', {'eventos': eventos})

def perfis_list(request):
    perfis = Perfil.objects.all()
    return render(request, 'content/perfis_list.html', {'perfis': perfis})

def perfil_novo(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            perfil = form.save()
            perfil.save()
            return HttpResponseRedirect('/perfis/')
    else:
        form = PerfilForm()
    return render(request, 'content/perfis_list.html', {'form': form})

def pyladiesday_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'content/pyladiesday_eventos.html', {'eventos': eventos})


