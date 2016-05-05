from django.shortcuts import render_to_response,redirect, RequestContext
from django.views.decorators.csrf import csrf_exempt

from time_tracker.models import Activities
from time_tracker.forms import AddActivityForm
from django.core.context_processors import csrf


def index(request):
    return render_to_response('main.html', context_instance=RequestContext(request))


def activities_list(request, username=''):

    return render_to_response('activities.html', {'activities': Activities.objects.filter(activities_user=username)},
                              context_instance=RequestContext(request))


def add_template(request, username=''):
    return render_to_response('add_activity.html')


@csrf_exempt
def add_activity(request, username=''):
    args = {}
    args.update(csrf(request))
    if request.POST:
        form = AddActivityForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = AddActivityForm()
    this_redirect = '/users/' + username + '/activities/all/'
    return redirect(this_redirect)
        
