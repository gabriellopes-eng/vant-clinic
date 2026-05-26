from django.core.exceptions import ValidationError
from django.db import models

from clientes.models import Cliente
from profissionais.models import Profissional
from servicos.models import ServicoEstetico


class Agendamento(models.Model):
	class StatusAgendamento(models.TextChoices):
		AGENDADO = "AGENDADO", "Scheduled"
		CANCELADO = "CANCELADO", "Cancelled"
		CONCLUIDO = "CONCLUIDO", "Completed"

	cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="agendamentos")
	profissional = models.ForeignKey(Profissional, on_delete=models.PROTECT, related_name="agendamentos")
	servico = models.ForeignKey(ServicoEstetico, on_delete=models.PROTECT, related_name="agendamentos")
	data_hora = models.DateTimeField()
	observacoes = models.TextField(blank=True)
	status = models.CharField(max_length=10, choices=StatusAgendamento.choices, default=StatusAgendamento.AGENDADO)
	criado_em = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-data_hora"]
		constraints = [
			models.UniqueConstraint(
				fields=["profissional", "data_hora"],
				condition=~models.Q(status="CANCELADO"),
				name="uq_agendamento_profissional_horario_ativo",
			),
		]

	def clean(self):
		super().clean()

		if self.status == self.StatusAgendamento.CANCELADO:
			return

		conflito = Agendamento.objects.filter(
			profissional=self.profissional,
			data_hora=self.data_hora,
		).exclude(pk=self.pk).exclude(status=self.StatusAgendamento.CANCELADO).exists()

		if conflito:
			raise ValidationError(
				{"data_hora": "This professional already has an appointment at this time."}
			)

	def save(self, *args, **kwargs):
		self.full_clean()
		return super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.cliente} - {self.servico} ({self.data_hora:%d/%m/%Y %H:%M})"
