from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from cadastro.models import *
from cadastro.serializers import *

# Create your views here.
class AlunoViewSet(viewsets.ViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def list(self, request):
        try:
            if request.method == "GET":
                alunos = Aluno.objects.all()
                data = [{
                    "id": aluno.id,
                    "nome": aluno.nome,
                    "cpf": aluno.cpf,
                    "email": aluno.email,
                    "empresa_id": aluno.empresa_id,
                    "telefone": aluno.telefone,
                    "data_nascimento": aluno.data_nascimento
                } for aluno in alunos]
                return Response(data)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        aluno = get_object_or_404(self.queryset, pk=pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)


    def create(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Aluno criado com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            aluno = Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response({"error": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AlunoSerializer(aluno, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Aluno atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            aluno = Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response({"error": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        aluno.delete()
        return Response({"message": "Aluno deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)

class CursoViewSet(viewsets.ViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def list(self, request):
        try:
            if request.method == "GET":
                cursos = Curso.objects.all()
                data = [{
                    "id": curso.id,
                    "nome": curso.nome,
                    "valor": curso.valor,
                    "descricao": curso.descricao,
                    "quant_dias": curso.quant_dias,
                } for curso in cursos]
                return Response(data)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        curso = get_object_or_404(self.queryset, pk=pk)
        serializer = CursoSerializer(curso)
        return Response(serializer.data)

    def create(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Curso criado com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            curso = Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            return Response({"error": "Curso não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CursoSerializer(curso, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Curso atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            curso = Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            return Response({"error": "Curso não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        curso.delete()
        return Response({"message": "Curso deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
    
class EmpresaViewSet(viewsets.ViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def list(self, request):
        try:
            if request.method == "GET":
                empresas = Empresa.objects.all()
                data = [{
                    "id": empresa.id,
                    "nome": empresa.nome,
                    "cnpj": empresa.cnpj,
                    "tipo_inscricao": empresa.tipo_inscricao,
                    "endereco": empresa.endereco,
                    "optante_simp_nacional": empresa.optante_simp_nacional,
                } for empresa in empresas]
                return Response(data)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Empresa criada com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({"error": "Empresa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Empresa atualizada com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({"error": "Empresa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        empresa.delete()
        return Response({"message": "Empresa deletada com sucesso!"}, status=status.HTTP_204_NO_CONTENT)

class EmpresaViewSet(viewsets.ViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def list(self, request):
        try:
            if request.method == "GET":
                empresas = Empresa.objects.all()
                data = [{
                    "id": empresa.id,
                    "nome": empresa.nome,
                    "cnpj": empresa.cnpj,
                    "tipo_inscricao": empresa.tipo_inscricao,
                    "endereco": empresa.endereco,
                    "optante_simp_nacional": empresa.optante_simp_nacional,
                } for empresa in empresas]
                return Response(data)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Empresa criada com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({"error": "Empresa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Empresa atualizada com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({"error": "Empresa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        empresa.delete()
        return Response({"message": "Empresa deletada com sucesso!"}, status=status.HTTP_204_NO_CONTENT)