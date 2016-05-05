from django.conf.urls import include, url
from django.contrib import admin
import time_tracker


urlpatterns = [
    # Examples:
    # url(r'^$', 'project_time_tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'time_tracker.views.index'),
    url(r'(?P<username>\w+)/activities/all/', 'time_tracker.views.activities_list'),
    url(r'(?P<username>\w+)/activities/create/','time_tracker.views.add_template'),

]