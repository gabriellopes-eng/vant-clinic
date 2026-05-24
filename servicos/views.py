from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ServicoEsteticoForm
from .models import ServicoEstetico


class ServicoEsteticoListView(ListView):
	model = ServicoEstetico
	template_name = "servicos/servico_list.html"
	context_object_name = "servicos"


class ServicoEsteticoCreateView(CreateView):
	model = ServicoEstetico
	form_class = ServicoEsteticoForm
	template_name = "servicos/servico_form.html"
	success_url = reverse_lazy("servicos:servico_list")


class ServicoEsteticoUpdateView(UpdateView):
	model = ServicoEstetico
	form_class = ServicoEsteticoForm
	template_name = "servicos/servico_form.html"
	success_url = reverse_lazy("servicos:servico_list")


class ServicoEsteticoDeleteView(DeleteView):
	model = ServicoEstetico
	template_name = "servicos/servico_confirm_delete.html"
	success_url = reverse_lazy("servicos:servico_list")
