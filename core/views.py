from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import RegisterForm


def home(request):
	return render(request, "core/home.html")


def register(request):
	if request.user.is_authenticated:
		return redirect("core:home")

	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Account created successfully.")
			return redirect("core:home")
	else:
		form = RegisterForm()

	return render(request, "registration/register.html", {"form": form})
