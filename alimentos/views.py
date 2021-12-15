from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AlimentoSerializable, MascotaSerializable
from .models import Alimento, Mascota

# Create your views here.
class AlimentoVista(viewsets.ModelViewSet):
    serializer_class: AlimentoSerializable
    queryset = Alimento.objects.all()

class MascotaVista(viewsets.ModelViewSet):
    serializer_class: MascotaSerializable
    queryset = Mascota.objects.all()