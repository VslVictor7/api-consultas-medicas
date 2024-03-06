from rest_framework import serializers
from .models import Profissional, Consulta

class CadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class ProfSerializer(serializers.ModelSerializer):
    id_prof = CadSerializer(read_only=True, many=True)
    class Meta:
        model = Profissional
        fields = '__all__'


