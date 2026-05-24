from django.db import models


class ServicoEstetico(models.Model):
	nome = models.CharField(max_length=120)
	descricao = models.TextField(blank=True)
	duracao_minutos = models.PositiveIntegerField()
	preco = models.DecimalField(max_digits=10, decimal_places=2)
	ativo = models.BooleanField(default=True)
	criado_em = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["nome"]

	def __str__(self):
		return self.nome
