from django.db import models

# Create your models here.

class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    tipo_inscricao = models.CharField(max_length=13, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    optante_simp_nacional = models.BooleanField(default=False, null=True, blank=True)

class Aluno(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    email = models.CharField(max_length=70, null=False, blank=False, unique=True)
    empresa_id = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.RESTRICT)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.email})"

class Curso(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    quant_dias = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Turma(models.Model):
    id = models.IntegerField(primary_key=True)
    curso_id = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.RESTRICT)
    localidade = models.TextField(null=False, blank=False)
    data_inicio = models.DateField(null=False, blank=False)
    data_fim = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class TurmaAluno(models.Model):
    id = models.IntegerField(primary_key=True)
    turma_id = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.RESTRICT)
    aluno_id = models.ForeignKey(Aluno, null=False, blank=False, on_delete=models.RESTRICT)
    
class Aula(models.Model):
    id = models.IntegerField(primary_key=True)
    turma_id = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.RESTRICT)
    qr_code_path = models.TextField(blank=False, null=False)
    data = models.DateField(null=False, blank=False)

class Pagamento(models.Model):
    id = models.IntegerField(primary_key=True)
    aluno_id = models.ForeignKey(Aluno, null=False, blank=False, on_delete=models.RESTRICT)
    curso_id = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.RESTRICT)
    status = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Matricula(models.Model):
    id = models.IntegerField(primary_key=True)
    aula_id = models.ForeignKey(Aluno, null=False, blank=False, on_delete=models.RESTRICT)
    turma_id = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.RESTRICT)
    fonte = models.CharField(max_length=100, null=False, blank=False)
    data_matricula = models.DateField(null=False, blank=False)

class Frequencia(models.Model):
    id = models.IntegerField(primary_key=True)
    aula_id = models.ForeignKey(Aula, null=False, blank=False, on_delete=models.RESTRICT)
    matricula_id = models.ForeignKey(Matricula, null=False, blank=False, on_delete=models.RESTRICT)
    presente = models.BooleanField(default=False, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)