from django.db import models

# Create your models here.

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    tipo_inscricao = models.CharField(max_length=13, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    optante_simp_nacional = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome} ({self.id})"

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    quant_dias = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.id})"

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    curso_id = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.RESTRICT)
    localidade = models.TextField(null=False, blank=False)
    data_inicio = models.DateField(null=False, blank=False)
    data_fim = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Turma - {self.id} / Curso - {self.curso_id.nome}"

class Aula(models.Model):
    id = models.AutoField(primary_key=True)
    qr_code_path = models.TextField(blank=False, null=False)
    data = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"Aula ({self.id})"

class Pagamento(models.Model):
    id = models.AutoField(primary_key=True)
    aluno_id = models.ForeignKey(Aluno, null=False, blank=False, on_delete=models.RESTRICT)
    curso_id = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.RESTRICT)
    status = models.CharField(max_length=50, null=False, blank=False)
    tipo_pagamento = models.CharField(max_length=50, null=False, blank=False, default='Pix')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pagamento - {self.id} / Status ({self.status})"

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    aluno_id = models.ForeignKey(Aluno, null=False, blank=False, on_delete=models.RESTRICT)
    turma_id = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE)
    fonte = models.CharField(max_length=100, null=False, blank=False)
    data_matricula = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"Matricula - {self.id} / Turma - ({self.turma_id}) / Aluno(a) - {self.aluno_id.nome}"

class Frequencia(models.Model):
    id = models.AutoField(primary_key=True)
    aula_id = models.ForeignKey(Aula, null=False, blank=False, on_delete=models.CASCADE)
    matricula_id = models.ForeignKey(Matricula, null=False, blank=False, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        condicao = "presente" if self.presente else "ausente"
        return f"{self.matricula_id.aluno_id.nome} está {condicao}"