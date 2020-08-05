from django import forms
from importlib_metadata.docs.conf import exclude_patterns

from job.models import Apply, Job


class ApplyForms(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'cv', 'website', 'cover_letter']


class Jo_Form(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug','owner',)
