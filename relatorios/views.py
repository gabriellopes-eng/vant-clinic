from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from agendamentos.models import Agendamento
from pagamentos.models import Pagamento
from servicos.models import ServicoEstetico


class RelatorioResumoView(LoginRequiredMixin, TemplateView):
	template_name = "relatorios/resumo.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		total_agendamentos = Agendamento.objects.count()
		total_cancelamentos = Agendamento.objects.filter(
			status=Agendamento.StatusAgendamento.CANCELADO
		).count()
		total_servicos = ServicoEstetico.objects.count()
		total_pagamentos = Pagamento.objects.count()
		valor_total_pago = Pagamento.objects.filter(
			status=Pagamento.StatusPagamento.PAGO
		).aggregate(total=Sum("valor"))["total"] or 0

		context.update(
			{
				"total_agendamentos": total_agendamentos,
				"total_cancelamentos": total_cancelamentos,
				"total_servicos": total_servicos,
				"total_pagamentos": total_pagamentos,
				"valor_total_pago": valor_total_pago,
			}
		)
		return context
