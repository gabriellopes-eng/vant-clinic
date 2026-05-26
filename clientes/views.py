from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ClienteForm
from .models import Cliente


class ClienteListView(LoginRequiredMixin, ListView):
	model = Cliente
	template_name = "clientes/cliente_list.html"
	context_object_name = "clientes"


class ClienteCreateView(LoginRequiredMixin, CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name = "clientes/cliente_form.html"
	success_url = reverse_lazy("clientes:cliente_list")


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
	model = Cliente
	form_class = ClienteForm
	template_name = "clientes/cliente_form.html"
	success_url = reverse_lazy("clientes:cliente_list")


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
	model = Cliente
	template_name = "clientes/cliente_confirm_delete.html"
	success_url = reverse_lazy("clientes:cliente_list")
