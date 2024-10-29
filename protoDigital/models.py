from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    CPF = models.CharField(max_length=255)
    RG = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    data_nascimento = models.DateField()
    CEP = models.IntegerField()
    endereco_usuario_rua = models.CharField(max_length=255)
    endereco_usuario_numero = models.IntegerField()
    endereco_usuario_complemento = models.CharField(
        max_length=255, blank=True, null=True)
    endereco_usuario_bairro = models.CharField(max_length=255)
    endereco_usuario_cidade = models.CharField(max_length=255)
    endereco_usuario_estado = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    usafa = models.ForeignKey(
        'Usafa', on_delete=models.CASCADE, related_name='usuarios')

    class Meta:
        db_table = 'USUARIO'


class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    data = models.DateField()
    horario = models.TimeField()
    tipo_consulta = models.CharField(max_length=255)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='consultas')

    class Meta:
        db_table = 'CONSULTA'


class Usafa(models.Model):
    id_usafa = models.AutoField(primary_key=True)
    nome_usafa = models.CharField(max_length=255)
    endereco_usafa_rua = models.CharField(max_length=255)
    endereco_usafa_numero = models.IntegerField()
    endereco_usafa_complemento = models.CharField(
        max_length=255, blank=True, null=True)
    endereco_usafa_bairro = models.CharField(max_length=255)
    endereco_usafa_cidade = models.CharField(max_length=255)
    endereco_usafa_estado = models.CharField(max_length=255)
    CEP_usafa = models.IntegerField()

    class Meta:
        db_table = 'USAFA'
