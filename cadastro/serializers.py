from rest_framework import serializers
from cadastro.models import *

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'id',
            'nome',
            'cpf',
            'email',
            'empresa_id',
            'telefone',
            'data_nascimento',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = [
            'id',
            'nome',
            'valor',
            'descricao',
            'quant_dias',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'id',
            'nome',
            'cnpj',
            'tipo_inscricao',
            'endereco',
            'optante_simp_nacional',
        ]
        read_only_fields = ['id']