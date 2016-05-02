from django.conf.urls import include, url
from django.contrib import admin
from login_register import urls
from time_tracker import urls
import login_register
import time_tracker
urlpatterns = [
    # Examples:
    # url(r'^$', 'project_time_tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include(login_register.urls)),
    url(r'', include(time_tracker.urls)),
    url(r'^users/', include(time_tracker.urls)),


]
