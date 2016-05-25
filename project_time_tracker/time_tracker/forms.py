from django import forms
from time_tracker.models import Activities
import datetime


class ActivityAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        self.new = kwargs.pop("new", None)
        self.activities_user = kwargs.pop("activities_user", None)
        super(ActivityAddForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ActivityAddForm, self).save(commit=False)
        instance.new = self.new
        instance.activities_user = self.activities_user
        instance.activities_duration = datetime.timedelta()
        instance.activities_duration = self.fields['activities_end'] - self.fields['activities_start']
        instance.add_date = datetime.datetime.now()
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Activities
        fields = ('activities_name', 'activities_type', 'activities_start', 'activities_end')


