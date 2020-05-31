from rest_framework import serializers
from .models import Receta

class RecetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receta
        fields = ['id_receta', 'fecha_receta', 'rut_paciente', 'rut_medico']