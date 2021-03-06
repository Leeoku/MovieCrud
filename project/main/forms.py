from django import forms
from django.forms import ModelForm
from django.db import models
from datetime import datetime
from .models import MovieEntry
import datetime

current_year = datetime.date.today().year

class MovieForm(ModelForm):
    class Meta:
        model = MovieEntry
        fields = '__all__'
        widgets = {
            'date_watched':forms.DateInput(format=('%y,%m,%d'), attrs={'class':'form-control-sm', 'type':'date'}),
            }