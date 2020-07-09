from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='SoccerHome'),  # home page main app
    path('Teams', views.team_home, name='SoccerTeam'),
    #path('viewTeams', views.create_home, name='SoccerTeamCreate'),
    path('register', views.register_page, name='registerPage'),
    path('Player', views.player_register, name='registerForPlayer'),  # Registering page path for a player
    path('team', views.team_register, name='registerForTeam'),  # Registering page Path for a team
    path('coach', views.coach_register, name='registerForCoach'),  # Registering page Path for a Coaches
    path('referee', views.referee_register, name='registerForReferee'),  # Registering page Path for a Referee
    path('tournament', views.tournament_register, name='registerForTournament'),  # Registering page Path for Tournament
    path('details', views.details_page, name='DetailsPage'),
    path('<int:pk>/PlayerDetail/', views.player_details, name="PlayerDetails"),
    path('<int:pk>/TeamDetail/', views.team_details, name="TeamDetails"),
    path('<int:pk>/CoachDetail/', views.coach_details, name="CoachDetails"),
    path('<int:pk>/RefereeDetail/', views.referee_details, name="RefereeDetails"),
    path('<int:pk>/TournamentDetail/', views.tournament_details, name="TournamentDetails"),
    path('<int:pk>/PlayerDelete/', views.player_delete, name="PlayerDelete"),
    path('<int:pk>/CoachDelete/', views.coach_delete, name="CoachDelete"),
    path('<int:pk>/RefereeDelete/', views.referee_delete, name="RefereeDelete"),
    path('<int:pk>/TournamentDelete/', views.tournament_delete, name="TournamentDelete"),
    path('<int:pk>/TeamDelete/', views.team_delete, name="TeamDelete")
]
