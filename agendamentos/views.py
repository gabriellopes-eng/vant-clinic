from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from .forms import AgendamentoForm
from .models import Agendamento


class AgendamentoListView(LoginRequiredMixin, ListView):
	model = Agendamento
	template_name = "agendamentos/agendamento_list.html"
	context_object_name = "agendamentos"


class AgendamentoCreateView(LoginRequiredMixin, CreateView):
	model = Agendamento
	form_class = AgendamentoForm
	template_name = "agendamentos/agendamento_form.html"
	success_url = reverse_lazy("agendamentos:agendamento_list")


class AgendamentoUpdateView(LoginRequiredMixin, UpdateView):
	model = Agendamento
	form_class = AgendamentoForm
	template_name = "agendamentos/agendamento_form.html"
	success_url = reverse_lazy("agendamentos:agendamento_list")


class AgendamentoCancelarView(LoginRequiredMixin, View):
	def post(self, request, pk):
		agendamento = get_object_or_404(Agendamento, pk=pk)
		agendamento.status = Agendamento.StatusAgendamento.CANCELADO
		agendamento.save(update_fields=["status"])
		return redirect("agendamentos:agendamento_list")
