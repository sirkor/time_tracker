from django.shortcuts import render_to_response,redirect
from time_tracker.models import Activities

def index(request):
    return render_to_response('main.html')


def activities_list(request):
    activities = Activities.objects.all()