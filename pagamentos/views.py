from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import PagamentoForm
from .models import Pagamento


class PagamentoListView(LoginRequiredMixin, ListView):
	model = Pagamento
	template_name = "pagamentos/pagamento_list.html"
	context_object_name = "pagamentos"


class PagamentoCreateView(LoginRequiredMixin, CreateView):
	model = Pagamento
	form_class = PagamentoForm
	template_name = "pagamentos/pagamento_form.html"
	success_url = reverse_lazy("pagamentos:pagamento_list")


class PagamentoUpdateView(LoginRequiredMixin, UpdateView):
	model = Pagamento
	form_class = PagamentoForm
	template_name = "pagamentos/pagamento_form.html"
	success_url = reverse_lazy("pagamentos:pagamento_list")


class PagamentoDeleteView(LoginRequiredMixin, DeleteView):
	model = Pagamento
	template_name = "pagamentos/pagamento_confirm_delete.html"
	success_url = reverse_lazy("pagamentos:pagamento_list")
