from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length= 50)

    class Meta:
        db_table = "fornecedor"


class Tipo_Medida(models.Model):
    descricao = models.CharField(max_length= 50)

    class Meta:
        db_table = "tipo_medida"


class Produto(models.Model):
    nome = models.CharField(max_length= 50)
    media_valor = models.FloatField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    tipo_media = models.ForeignKey(Tipo_Medida, on_delete=models.CASCADE)

    class Meta:
        db_table = "produto"


class Tipo_Movimentacao(models.Model):
    descricao = models.CharField(max_length= 50)

    class Meta:
        db_table = "tipo_movimentacao"


class Cliente(models.Model):
    nome = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)
    rua = models.CharField(max_length= 50)
    cep = models.CharField(max_length= 50)
    
    class Meta:
        db_table = "cliente"

    
class Movimentacao(models.Model):
    quantidade = models.CharField(max_length= 50)
    data_entrada = models.CharField(max_length= 50)
    data_saida = models.CharField(max_length= 50)
    tipo_movimentacao = models.ForeignKey(Tipo_Movimentacao, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    class Meta:
        db_table = "movimentacao"


class Doumento(models.Model):
    movimentacao = models.ForeignKey(Movimentacao, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = "documento"


class Tipo_Deposito(models.Model):
    descricao = models.CharField(max_length= 50)

    class Meta:
        db_table = "tipo_deposito"


class Filial(models.Model):
    nome = models.CharField(max_length= 50)

    class Meta:
        db_table = "filial"


class Local(models.Model):
    nome = models.CharField(max_length= 50)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)

    class Meta:
        db_table = "local"


class Deposito(models.Model):
    nome = models.CharField(max_length= 50)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    tipo_deposito = models.ForeignKey(Tipo_Deposito, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

    class Meta:
        db_table = "deposito"









