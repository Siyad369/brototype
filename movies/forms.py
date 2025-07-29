from django import forms
from . models import MovieInfo,CensorInfo


class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieInfo
        fields = '__all__'


class CensorForm(forms.ModelForm):
    class Meta:
        model = CensorInfo
        fields = '__all__'

