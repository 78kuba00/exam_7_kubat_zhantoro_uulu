from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        # widgets = {'variation': widgets.Select}

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['variation']
        exclude = ['poll']

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')