from django.shortcuts import render_to_response,redirect
from time_tracker.models import Activities

def index(request):
    return render_to_response('main.html')


def activities_list(request, username=''):
    args = username
    list_of_activities = Activities.objects.filter(activities_user=username)
    return render_to_response('activities.html', list_of_activities)