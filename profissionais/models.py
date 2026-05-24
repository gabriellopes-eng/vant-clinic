from django.db import models


class Profissional(models.Model):
	nome = models.CharField(max_length=120)
	especialidade = models.CharField(max_length=120, blank=True)
	telefone = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)
	ativo = models.BooleanField(default=True)
	criado_em = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["nome"]

	def __str__(self):
		return self.nome
