from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ProfissionalForm
from .models import Profissional


class ProfissionalListView(ListView):
	model = Profissional
	template_name = "profissionais/profissional_list.html"
	context_object_name = "profissionais"


class ProfissionalCreateView(CreateView):
	model = Profissional
	form_class = ProfissionalForm
	template_name = "profissionais/profissional_form.html"
	success_url = reverse_lazy("profissionais:profissional_list")


class ProfissionalUpdateView(UpdateView):
	model = Profissional
	form_class = ProfissionalForm
	template_name = "profissionais/profissional_form.html"
	success_url = reverse_lazy("profissionais:profissional_list")


class ProfissionalDeleteView(DeleteView):
	model = Profissional
	template_name = "profissionais/profissional_confirm_delete.html"
	success_url = reverse_lazy("profissionais:profissional_list")
