from django.db import models


class Cliente(models.Model):
    cnpj = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.razao_social


class Produto(models.Model):
    sku = models.CharField(max_length=45, unique=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class CondicaoPagamento(models.Model):
    descricao = models.CharField(max_length=45)
    dias = models.IntegerField()

    def __str__(self):
        return self.descricao


class PrecoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cliente} - {self.produto} - R$ {self.valor}"


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    condicao_pagamento = models.ForeignKey(CondicaoPagamento, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venda {self.id}"


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)


class Notificacao(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    mensagem = models.TextField()

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensagem