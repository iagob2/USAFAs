from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import BaseBackend
import logging


logger = logging.getLogger(__name__)

class CPFBackend(BaseBackend):
    def authenticate(self, request, cpf=None, password=None):
        logger.debug(f"Tentando autenticar com CPF: {cpf} e senha: {password}")
        try:
            usuario = Usuario.objects.get(CPF=cpf)
            if usuario.senha == password:
                return usuario
            logger.debug(f"Senha incorreta para o CPF: {cpf}")
            return None
        except Usuario.DoesNotExist:
            logger.debug(f"Usuário com CPF: {cpf} não encontrado")
            return None





class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    CPF = models.CharField(max_length=255)
    RG = models.CharField(max_length=255)
    senha = models.CharField(max_length=128, default="123456", null=True, blank=True)
    nome_usuario = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    CEP = models.CharField(max_length=9)
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

    def save(self, *args, **kwargs):
        # Criptografa a senha antes de salvar no banco
        if self.senha:
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)


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
    telefone_usafa = models.CharField(max_length=255)
    endereco_usafa_rua = models.CharField(max_length=255)
    endereco_usafa_numero = models.IntegerField()
    endereco_usafa_complemento = models.CharField(
        max_length=255, blank=True, null=True)
    endereco_usafa_bairro = models.CharField(max_length=255)
    CEP_usafa = models.IntegerField()

    class Meta:
        db_table = 'USAFA'
