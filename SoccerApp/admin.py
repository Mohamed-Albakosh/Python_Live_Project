from django.contrib import admin

from . import models
from .models import Team, Players, Referees, Coaches, SoccerMatch

# Register your models here.
myModels = [models.Team, models.Players, models.Referees, models.Coaches, models.SoccerMatch]  # iterable list
admin.site.register(myModels)
