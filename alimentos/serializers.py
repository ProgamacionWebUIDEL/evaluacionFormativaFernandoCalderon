from django.db.models import fields
from rest_framework import serializers
from .models import Alimento, Mascota

class AlimentoSerializable(serializers.ModelSerializer):
    class Meta:

        model = Alimento
        fields = (
            'nomAlimento', 
            'tipoAlimento',
            'numCalorias'
        )

class MascotaSerializable(serializers.ModelSerializer):
    class Meta:

        model = Mascota
        fields = (
            'nomMascota', 
            'razaMascota',
            'pesoMascota'
        )