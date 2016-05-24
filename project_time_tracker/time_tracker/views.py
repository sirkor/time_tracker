from django.shortcuts import render_to_response, redirect, RequestContext
from time_tracker.models import Activities
import datetime
from time_tracker.forms import ActivityAddForm
from django.db.models import Sum, DurationField


def index(request):
    """Index page"""
    return render_to_response('main.html', context_instance=RequestContext(request))


def activities_list(request, username=''):
    """ list of user activities  """
    args = {'activities': Activities.objects.filter(activities_user=username)}
    return render_to_response('activities.html', args, context_instance=RequestContext(request))


def thanks_view(request):
    """ success view for add_activity """
    return render_to_response('thanks.html', context_instance=RequestContext(request))


def statistic(request, username=''):
    """View for statistic """
    if request.user.username == username:
        now = datetime.datetime.now()
        new_now = datetime.datetime.now()
        cur_year = now.year
        cur_month = now.month
        start = now.replace(year=cur_year, month=cur_month, day=1)
        end = new_now.replace(year=cur_year, month=cur_month, day=30)
        all_duration = Activities.objects.filter(new=request.user).exclude(
            add_date__lte=start, add_date__gte=end).aggregate(sum=Sum('activities_duration',
                                                                      output_field=DurationField()))

        work_duration = Activities.objects.filter(new=request.user, activities_type="Работа").exclude(
            add_date__lte=start, add_date__gte=end).aggregate(sum=Sum('activities_duration',
                                                                      output_field=DurationField()))

        other_duration = Activities.objects.filter(new=request.user).exclude(activities_type="Работа",
                                                                             add_date__lte=start, add_date__gte=end).\
            aggregate(sum=Sum('activities_duration', output_field=DurationField()))

        percent_of_work_duration = work_duration['sum'] / all_duration['sum'] * 100
        percent_of_other_duration = other_duration['sum'] / all_duration['sum'] * 100
        args = {'sum_duration': all_duration['sum'], 'work_duration': work_duration['sum'],
                'other_duration': other_duration['sum'],
                'percent_of_work_duration': round(percent_of_work_duration, 2),
                'percent_of_other_duration': round(percent_of_other_duration, 2)}
        return render_to_response('statistic.html', args, context_instance=RequestContext(request))

    return render_to_response('statistic.html', context_instance=RequestContext(request))


def add_activity(request, username=''):
    """view for form ActivityAddForm"""
    if request.POST:
        form = ActivityAddForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.new = request.user
            activity.activities_user = username
            activity.activities_duration = activity.activities_end - activity.activities_start
            activity.add_date = datetime.datetime.now()
            activity.save()
            return redirect('/thanks/')
    else:
        form = ActivityAddForm()
        args = {'form': form}
    return render_to_response('add_activity.html', args, context_instance=RequestContext(request))


