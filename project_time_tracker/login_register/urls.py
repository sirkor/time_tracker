from django.conf.urls import include, url
from django.contrib import admin
import login_register
from login_register import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project_time_tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', views.LoginFormView.as_view()),
    url(r'^logout/', 'login_register.views.logout'),
    url(r'^register/$', views.RegisterFormView.as_view()),

]
