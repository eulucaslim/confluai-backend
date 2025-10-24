from rest_framework import serializers
from cadastro.models import Aluno

class AlunoSerializer(serializers.Serializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email']