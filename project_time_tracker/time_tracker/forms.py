from django import forms
from .models import Activities
from django.contrib.auth.models import User


class AddActivityForm(forms.Form):
    activities_name = forms.CharField(label="Название", max_length=30)
    activities_type = forms.CharField(label="Тип", max_length=30)
    activities_start = forms.DateTimeField(label="Время начала")
    activities_end = forms.DateTimeField(label="Время окончания")






















