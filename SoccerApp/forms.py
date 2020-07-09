# noinspection PyUnresolvedReferences

from django import forms
from django.forms import ModelForm

from .models import Team, Players, Referees, Coaches, SoccerMatch


class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = '__all__'


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class RefereesForm(ModelForm):
    class Meta:
        model = Referees
        fields = '__all__'


class CoachesForm(ModelForm):
    class Meta:
        model = Coaches
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'Time'


class SoccerMachForm(forms.ModelForm):
    class Meta:
        model = SoccerMatch
        fields = '__all__'
        widgets = {'MatchDate': DateInput(), 'MatchTime': TimeInput()}
