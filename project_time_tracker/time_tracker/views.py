from django.shortcuts import render_to_response,redirect, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from time_tracker.models import Activities
from time_tracker.forms import AddActivityForm
from django.core.context_processors import csrf


def index(request):
    return render_to_response('main.html', context_instance=RequestContext(request))


def activities_list(request, username=''):

    return render_to_response('activities.html', {'activities': Activities.objects.filter(activities_user=username)},
                              context_instance=RequestContext(request))


def thanks_view(request):
    return render_to_response('thanks.html', context_instance=RequestContext(request))


def add_template(request, username=''):
    return render_to_response('add_activity.html', context_instance=RequestContext(request))


class AddActivityFormView(FormView):
    template_name = 'add_activity.html'
    form_class = AddActivityForm
    success_url = '/users/thanks/'

    def form_valid(self, form):

        return super(AddActivityFormView, self).form_valid(form)