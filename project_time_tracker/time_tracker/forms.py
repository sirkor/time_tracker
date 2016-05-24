from django import forms
from time_tracker.models import Activities


class ActivityAddForm(forms.ModelForm):

    class Meta:
        model = Activities
        fields = ('activities_name', 'activities_type', 'activities_start', 'activities_end')
