from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            args['login_error'] = "Пользователь найден"
            this_redirect = '/users/' + username + '/activities/all/'
            a = request
            return redirect(this_redirect)

        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)

    else:
        render_to_response('login.html', args)

    return render_to_response('login.html', args)


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
