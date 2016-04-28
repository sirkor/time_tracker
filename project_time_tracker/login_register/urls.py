from django.conf.urls import include, url
from django.contrib import admin
import login_register


urlpatterns = [
    # Examples:
    # url(r'^$', 'project_time_tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', 'login_register.views.login'),
    url(r'^logout/', 'login_register.views.logout'),
]