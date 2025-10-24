from rest_framework.response import Response
from rest_framework import viewsets
from cadastro.models import Aluno
from cadastro.serializers import AlunoSerializer

# Create your views here.


class AlunoViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            if request.method == "GET":
                queryset = Aluno.objects.all()
                data = [{
                    "id": aluno.id, 
                    "nome": aluno.nome
                } for aluno in queryset]
                return Response(data)
        except Exception as e:
            return Response({'error': e})
