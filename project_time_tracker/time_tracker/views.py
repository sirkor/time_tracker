from django.shortcuts import render_to_response, redirect, RequestContext
from time_tracker.models import Activities
import datetime


def index(request):
    return render_to_response('main.html',
                              context_instance=RequestContext(request))


def activities_list(request, username=''):
    args = {'activities': Activities.objects.filter(activities_user=username)}
    return render_to_response('activities.html',
                              args,
                              context_instance=RequestContext(request))


def thanks_view(request):
    return render_to_response('thanks.html',
                              context_instance=RequestContext(request))


def add_template(request, username=''):
    return render_to_response('add_activity.html',
                              context_instance=RequestContext(request))


def add_activity_view(request, username=''):
    if request.POST:
        name = request.POST.get('activities_name', '')
        my_type = request.POST.get('activities_type', '')
        start = request.POST.get('activities_start', '')
        end = request.POST.get('activities_end', '')
        new_start = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M")
        new_end = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M")
        duration = new_end - new_start
        new_post = Activities(activities_user=username,
                              activities_name=name,
                              activities_type=my_type,
                              activities_start=start,
                              activities_end=end, activities_duration=duration,
                              new=request.user,
                              add_date=datetime.datetime.now())
        new_post.save()
        return redirect('/users/thanks')
    return render_to_response('add_activity.html',
                              context_instance=RequestContext(request))


def statistic_view(request, username=''):
    now = datetime.datetime.now()
    statistic = Activities.objects.\
        filter(activities_user=request.user.username)
    sum_of_duration = datetime.timedelta(0)
    for stat in statistic:
        if stat.activities_start.month == now.month:
            sum_of_duration += stat.activities_duration

    statistic = Activities.objects.\
        filter(activities_user=request.user.username, activities_type='Работа')
    work_duration = datetime.timedelta(0)
    for stat in statistic:
        if stat.activities_start.month == now.month:
            work_duration += stat.activities_duration

    statistic = Activities.objects.\
        filter(activities_user=request.user.username,
               activities_type='Остальное')
    other_duration = datetime.timedelta(0)
    for stat in statistic:
        if stat.activities_start.month == now.month:
            other_duration += stat.activities_duration

    percent_of_work_duration = work_duration / sum_of_duration * 100
    percent_of_other_duration = other_duration / sum_of_duration * 100
    args = {'sum_duration': sum_of_duration, 'work_duration': work_duration,
            'other_duration': other_duration,
            'percent_of_work_duration': round(percent_of_work_duration, 2),
            'percent_of_other_duration': round(percent_of_other_duration, 2)}

    return render_to_response('statistic.html', args,
                              context_instance=RequestContext(request))
