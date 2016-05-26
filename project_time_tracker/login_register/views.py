from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm


def logout(request):
    auth.logout(request)
    return redirect("/")


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/auth/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        auth.login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
