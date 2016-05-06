from django.shortcuts import render_to_response,redirect, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView, CreateView
from time_tracker.models import Activities
from time_tracker.forms import AddActivityForm
from django.core.context_processors import csrf
from datetime import datetime


def index(request):
    return render_to_response('main.html', context_instance=RequestContext(request))


def activities_list(request, username=''):

    return render_to_response('activities.html', {'activities': Activities.objects.filter(activities_user=username)},
                              context_instance=RequestContext(request))


def thanks_view(request):
    return render_to_response('thanks.html', context_instance=RequestContext(request))


def add_template(request, username=''):
    return render_to_response('add_activity.html', context_instance=RequestContext(request))


'''class AddActivityFormView(CreateView):
    template_name = 'add_activity.html'
    form_class = AddActivityForm
    success_url = '/users/thanks/'

    def get_form_kwargs(self, step=None):
        kwargs = super(AddActivityFormView, self).get_form_kwargs(step)
        if step == '1':
            kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        return super(AddActivityFormView, self).form_valid(form)'''


def add_activity_view(request, username=''):
    if request.POST:
        name = request.POST.get('activities_name','')
        my_type = request.POST.get('activities_type', '')
        start = request.POST.get('activities_start', '')
        end = request.POST.get('activities_end', '')
        new_start = datetime.strptime(start, "%Y-%m-%d %H:%M")
        new_end = datetime.strptime(end, "%Y-%m-%d %H:%M")
        duration = new_end - new_start
        new_post = Activities(activities_user=username,activities_name=name,activities_type=my_type,activities_start=start,
                              activities_end=end, activities_duration=duration)
        new_post.save()
        return redirect('/users/thanks')
    return render_to_response('add_activity.html', context_instance=RequestContext(request))