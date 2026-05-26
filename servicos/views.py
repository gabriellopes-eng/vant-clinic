from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ServicoEsteticoForm
from .models import ServicoEstetico


class ServicoEsteticoListView(LoginRequiredMixin, ListView):
	model = ServicoEstetico
	template_name = "servicos/servico_list.html"
	context_object_name = "servicos"


class ServicoEsteticoCreateView(LoginRequiredMixin, CreateView):
	model = ServicoEstetico
	form_class = ServicoEsteticoForm
	template_name = "servicos/servico_form.html"
	success_url = reverse_lazy("servicos:servico_list")


class ServicoEsteticoUpdateView(LoginRequiredMixin, UpdateView):
	model = ServicoEstetico
	form_class = ServicoEsteticoForm
	template_name = "servicos/servico_form.html"
	success_url = reverse_lazy("servicos:servico_list")


class ServicoEsteticoDeleteView(LoginRequiredMixin, DeleteView):
	model = ServicoEstetico
	template_name = "servicos/servico_confirm_delete.html"
	success_url = reverse_lazy("servicos:servico_list")
