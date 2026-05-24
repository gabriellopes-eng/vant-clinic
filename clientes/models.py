from django.db import models


class Cliente(models.Model):
	nome = models.CharField(max_length=120)
	telefone = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)
	observacoes = models.TextField(blank=True)
	ativo = models.BooleanField(default=True)
	criado_em = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["nome"]

	def __str__(self):
		return self.nome
