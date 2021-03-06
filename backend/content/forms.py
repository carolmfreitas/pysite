from django import forms 
from .models import Perfil
  
class PerfilForm(forms.ModelForm): 
  
    class Meta: 
        model = Perfil 
        fields = ('nome', 'email', 'city', 'profissao', 'linkedin', 'site', 'github', 'facebook', 'biografia', 'foto',)