# Python_Live_Project
 AppBuilder9000
<h2>Introduction</h2>

<p>In a  first two weeks of my time at the tech academy, I  worked with my peers in a team developing in a hoppy app every student get chance to develope the app from his choosen.
I get a chance to work so hard to develope my Soccer App using Python, Django, SQLite, and HTML/CSS. It  was a great learning oppertunity  it is a very good chance for me to create
An App in team project works spontaneously with others to repesent one project. In this project I get a great oppertunity to work back end and front end. for a a back end  I create
a model for my the collection items i get chance to design the database for my app and display the information from the database and delet the items fro database and edit it. also I 
get chance to work in front end design my page ad buttons frams also css designs.
 Everyone on the team had a chance to work on front end and back end stories. Over the two week sprint. Also  I had the opportunity to work on project management as Azur and team 
 programming skills that I'm confident I will use again and again on future projects. 
 
 Below are descriptions of the stories I worked on, along with code snippets and navigation links. I also have some full code files in this repo for the larger functionalities I
 implemented. </p>
 
 <h2>Back End for Stories</h2>
 <ul> 
     <a href="#code_model"><li>Create a Model</li></a>
     <a href="#code_form"><li>Create a Forms</li></a>
     <a href="#code_view"><li>Views Functions</li></a>
     <a href="#code_url"><li>Urls</li></a>
 </ul>
 <div id="code_model">
 <h3> This story about Create a model for the collection item  </h3>
 <p>Create a model and add a migration and Including an objects manager for accessing the database.</p>
 
 <pre>
    <code>
    "
    from django.db import models


# Create your models here.
class Team(models.Model):
    TeamName = models.CharField(max_length=100)

    teamOB = models.Manager()

    def __str__(self):
        return self.TeamName


class Players(models.Model):
    PlayerName = models.CharField(max_length=100)
    PlayerAddress = models.CharField(max_length=100)
    PlayerEmailAddress = models.CharField(max_length=100)
    PlayerPhoneNumber = models.IntegerField()
    TeamID = models.ForeignKey(Team, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.PlayerName


class Coaches(models.Model):
    CoachName = models.CharField(max_length=100)
    CoachAddress = models.CharField(max_length=100)
    CoachEmailAddress = models.CharField(max_length=100)
    CoachPhoneNumber = models.IntegerField()
    TeamID = models.ForeignKey(Team, on_delete=models.CASCADE)

    coachOB = models.Manager()

    def __str__(self):
        return self.CoachName


class Referees(models.Model):
    RefereeName = models.CharField(max_length=100)
    RefereeKind = models.CharField(max_length=100)
    RefereeAddress = models.CharField(max_length=100)
    RefereeEmailAddress = models.CharField(max_length=100)
    RefereePhoneNumber = models.IntegerField()

    RefereesOB = models.Manager()

    def __str__(self):
        return self.RefereeName


class SoccerMatch(models.Model):
    Team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Team_1')
    Team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Team_2')
    RefereeID = models.ForeignKey(Referees, on_delete=models.CASCADE)
    MatchAddress = models.CharField(max_length=100)
    MatchDate = models.DateField("Date(mm/dd/2020)", auto_now_add=False, auto_now=False, blank=True)
    MatchTime = models.TimeField()

    SoccerMatchOB = models.Manager()"
    </code>
 <pre>
 
 </div>
  <div id="code_form">
 <h3> Create a form class   </h3>
 <p>Create a form class  to intract with our models to accessing the database .</p>
 
 <pre>
    <code>
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
    </code>
 <pre>
 
 </div>
 <!-- Views -->
 <div id="code_view">
 <h3> views function </h3>
 <p>Create a views function that will find the single desired instance from the database and send it to the template.</p>
 
 <pre>
    <code>
from django.contrib.sites import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Team, Players, Referees, Coaches, SoccerMatch
from .forms import PlayersForm, TeamForm, RefereesForm, CoachesForm, SoccerMachForm


# View function that renders the home page,
def index(request):
    return render(request, 'SoccerApp/SoccerApp_home.html')


def team_home(request):
    teams = Team.teamOB.all()
    players = Players.objects.all()
    coaches = Coaches.coachOB.select_related('TeamID')
    referees = Referees.RefereesOB.all()
    soccer = SoccerMatch.SoccerMatchOB.all()
    return render(request, 'SoccerApp/SoccerApp_page.html', {'teams': teams, 'coaches': coaches, 'players': players,
                                                             'referees': referees, 'soccer': soccer})


def details_page(request):
    return render(request, 'SoccerApp/SoccerAppDetails.html')


def register_page(request):
    return render(request, 'SoccerApp/SoccerAppRegister.html')


# Register a player for a team
def player_register(request):
    form = PlayersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('SoccerTeam')
    else:
        # print(form.errors)
        form = PlayersForm()
    context = {
        'form': form,
    }
    return render(request, 'SoccerApp/Create_SoccerPlayer.html', context)


# adding a new Team
def team_register(request):
    form = TeamForm(request.POST or None)  # Gets the posted form, if one exists
    if form.is_valid():  # Checks the form for errors
        form.save()  # save to database
        return redirect('SoccerTeam')
    else:
        # print(form.errors)  # Prints any errors for the posted form
        form = TeamForm()
    context = {
        'form': form,
    }
    return render(request, 'SoccerApp/Create_SoccerTeam.html', context)


def coach_register(request):
    form = CoachesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('SoccerTeam')
    else:
        print(form.errors)
        form = CoachesForm()
    context = {
        'form': form,
    }
    return render(request, 'SoccerApp/Create_SoccerCoach.html', context)


def referee_register(request):
    form = RefereesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('SoccerTeam')
    else:
        messages.error(request, "Error")
        # print(form.errors)
        form = RefereesForm()
    context = {
        'form': form,
    }
    return render(request, 'SoccerApp/Create_SoccerReferee.html', context)


def tournament_register(request):
    form = SoccerMachForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('SoccerTeam')
    else:
        # print(form.errors)
        form = SoccerMachForm()
    context = {
        'form': form,
    }
    return render(request, 'SoccerApp/Create_SoccerTournament.html', context)


def team_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Team, pk=pk)
    team = TeamForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if team.is_valid():
            # form2 = team.save(commit=False)
            team.save()
            return redirect('SoccerTeam')
        else:
            print(team.errors)
    else:
        return render(request, 'SoccerApp/Create_TeamDetails.html', {'form': team})


def player_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Players, pk=pk)
    player = PlayersForm(data=request.POST or None, instance=item)

    if request.method == 'POST':
        if player.is_valid():
            # form2 = player.save(commit=False)
            player.save()
            print("form saved")
            return redirect('SoccerTeam')
        else:
            print("form not saved")
            print(player.errors)
    else:
        return render(request, 'SoccerApp/Create_playerDetails.html', {'form': player})


def coach_details(request, pk):
    pk = int(pk)
    item_2 = get_object_or_404(Coaches, pk=pk)
    coach = CoachesForm(data=request.POST or None, instance=item_2)
    if request.method == 'POST':
        if coach.is_valid():
            coach2 = coach.save(commit=False)
            coach2.save()
            return redirect('SoccerTeam')
        else:
            print(coach.errors)
    else:
        return render(request, 'SoccerApp/Create_CoachDetails.html', {'form': coach})


def referee_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Referees, pk=pk)
    referee = RefereesForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if referee.is_valid():
            # referee2 = referee.save(commit=False)
            referee.save()
            return redirect('SoccerTeam')
        else:
            print(referee.errors)
    else:
        return render(request, 'SoccerApp/Create_RefereeDetails.html', {'form': referee})


def tournament_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(SoccerMatch, pk=pk)
    tournament = SoccerMachForm(data=request.POST or None, instance=item)
    print(item.MatchTime)
    if request.method == 'POST':
        if tournament.is_valid():
            # tournament2 = tournament.save(commit=False)
            tournament.save()
            return redirect('SoccerTeam')
        else:
            print(tournament.errors)
    else:
        return render(request, 'SoccerApp/Create_TournamentDetails.html', {'form': tournament})


def player_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Players, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('SoccerTeam')
    context = {"item": item, }
    return render(request, "SoccerApp/confirmDelete.html", context)


def coach_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Coaches, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('SoccerTeam')
    context = {"item": item, }
    return render(request, "SoccerApp/confirmDelete.html", context)


def referee_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Referees, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('SoccerTeam')
    context = {"item": item, }
    return render(request, "SoccerApp/confirmDelete.html", context)


def tournament_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(SoccerMatch, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('SoccerTeam')
    context = {"item": item, }
    return render(request, "SoccerApp/confirmDelete.html", context)


def team_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('SoccerTeam')
    context = {"item": item, }
    return render(request, "SoccerApp/confirmDelete.html", context)


APIkey = "DqMevrmoG6WCCemH0gEKmB4GDN8uqhhYO6fSj1chBY1YUaILPv2cfzHqVYh7"


def api_index(request):
    url = "https://soccer.sportmonks.com/api/v2.0/players/search/__SEARCH__"
    # Print the status code of the response.
    response = requests.get(url, params={'api_token': APIkey})
    name = response.json(response)
    print(name)
    return render(request,)
    </code>
 <pre>
 
 </div>
 <!-- URLS -->
  
 
  <div id="code_url">
 <h3> urls   </h3>
 <p>urlpatterns" tuple here where we define the mapping between URLs and views</p>
 
 <pre>
    <code>
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



    </code>
 </pre>
 
  <h2>Front End for my Stories</h2>
  <p>for my front end work I will enclude all my templates pages edit Delete and display details from Database also i get a chance to add some css to my pages</p>
   <pre>
    <code>
    <!-- CoachDetail.html -->
    {% extends 'SoccerApp/SoccerApp_base.html' %}

    {% load staticfiles %}
    {% block templatecontent %}
    <div class="admin_panel">
        <form method="POST" id="thisForm" action="../CoachDetail/">
            <div class="frmObject_container">

                {% csrf_token %}
                {{ form.non_field_errors }}
                {{ form.as_table }}

            <div class="frmBtn_container">
                <input type="submit">
                   <a href="../{{ form.pk }}CoachDelete/"><button id="btn" type="button" >DELETE</button></a>
                    <a href="{% url 'SoccerTeam' %}"><button id="btn" type="button" >Cancel</button></a>
                </div>
            </div>
        </form>
    </div>
    {% endblock %}
 <!-- =========== PlayerDetail.html ============= -->
     {% extends 'SoccerApp/SoccerApp_base.html' %}

      {% load staticfiles %}
      {% block templatecontent %}
      <div class="admin_panel">
          <form method="POST" id="thisForm" action="../PlayerDetail/">
              <div class="frmObject_container">

                  {% csrf_token %}
                  {{ form.non_field_errors }}
                  {{ form.as_table }}

              <div class="frmBtn_container">
                  <input type="submit">
                  <a href="../{{ form.pk }}PlayerDelete/"><button id="btn" type="button" >DELETE</button></a>
                     <a href="{% url 'SoccerTeam'%}"> <button id="btn" type="button" >Cancel</button></a>
                  </div>
              </div>

          </form>
      </div>
      {% endblock %}
  <!-- =========== RefereeDetail.html =================-->   
      {% extends 'SoccerApp/SoccerApp_base.html' %}

      {% load staticfiles %}
      {% block templatecontent %}
      <div class="admin_panel">
          <form method="POST" id="thisForm" action="../RefereeDetail/">
              <div class="frmObject_container">

                  {% csrf_token %}
                  {{ form.non_field_errors }}
                  {{ form.as_table }}

              <div class="frmBtn_container">
                  <input type="submit">
                  <a href="../{{ form.pk }}RefereeDelete/"><button id="btn" type="button" >DELETE</button></a>
                     <a href="{% url 'SoccerTeam'%}"> <button id="btn" type="button" >Cancel</button></a>
                  </div>
              </div>

          </form>
      </div>
      {% endblock %}
      
      {% extends 'SoccerApp/SoccerApp_base.html' %}
      {% load staticfiles %}
      {% block templatecontent %}
      <div class="admin_panel">
              <form method="POST" action="{% url 'registerForCoach' %}">
                  <div class="frmObject_container">
                      <!-- Cross Site Request Forgery (csrf_token) protection -->
                      {% csrf_token %}
                      {{ form.non_field_errors }}
                      {{ form.as_p }}
                  </div>
                  <div class="frmBtn_container">
                      <input type="submit" id="btn" value="New Coach" name="Save_Item">
                      <a href="{% url 'registerPage' %}"><button type="button" id="btn" value="Cancel">Cancel</button></a>
                  </div>
              </form>
          </div>
      {% endblock %}
      
      {% extends 'SoccerApp/SoccerApp_base.html' %}

      {% load staticfiles %}
      {% block templatecontent %}
      <div class="admin_panel">
              <form method="POST" action="{% url 'registerForPlayer' %}">
                  <div class="frmObject_container">
                      <!-- Cross Site Request Forgery (csrf_token) protection -->
                      {% csrf_token %}
                      {{ form.non_field_errors }}
                      {{ form.as_p }}
                  </div>
                  <div class="frmBtn_container">
                      <input type="submit" id="btn" value="New Player" name="Save_Item">
                      <a href="{% url 'registerPage' %}"><button type="button" id="btn" value="Cancel">Cancel</button></a>
                  </div>
              </form>
          </div>
    
    
        {% endblock %}

        {% extends 'SoccerApp/SoccerApp_base.html' %}

        {% load staticfiles %}
        {% block templatecontent %}
        <div class="admin_panel">
                <form method="POST" action="{% url 'registerForReferee' %}">
                    <div class="frmObject_container">
                        <!-- Cross Site Request Forgery (csrf_token) protection -->
                        {% csrf_token %}
                        {{ form.non_field_errors }}
                        {{ form.as_p }}
                    </div>
                    <div class="frmBtn_container">
                        <input type="submit" id="btn" value="New Referee" name="Save_Item">
                        <a href="{% url 'registerPage' %}"><button type="button" id="btn" value="Cancel">Cancel</button></a>
                    </div>
                </form>
            </div>
        {% endblock %}
        
        {% extends 'SoccerApp/SoccerApp_base.html' %}

        {% load staticfiles %}
        {% block templatecontent %}
        <div class="admin_panel">
                <form method="POST" action="{% url 'registerForTeam' %}">
                    <div class="frmObject_container">
                        <!-- Cross Site Request Forgery (csrf_token) protection -->
                        {% csrf_token %}
                        {{ form.non_field_errors }}
                        {{ form.as_p }}
                    </div>
                    <div class="frmBtn_container">
                        <input type="submit" id="btn" value="New Team" name="Save_Item">
                        <a href="{% url 'registerPage' %}"><button type="button" id="btn" value="Cancel">Cancel</button></a>
                    </div>
                </form>
            </div>
        {% endblock %}
         
         {% extends 'SoccerApp/SoccerApp_base.html' %}

        {% load staticfiles %}
        {% block templatecontent %}

        <div class="admin_panel">
                <form method="POST" action="{% url 'registerForTournament' %}">
                    <div class="frmObject_container">
                        <!-- Cross Site Request Forgery (csrf_token) protection -->
                        {% csrf_token %}
                        {{ form.non_field_errors }}
                        {{ form.as_p }}
                    </div>
                    <div class="frmBtn_container">
                        <input type="submit" class="btn" value="New Team" name="Save_Item">
                        <a href="{% url 'registerPage' %}"><button type="button" id="btn" value="Cancel">Cancel</button></a>
                    </div>
                </form>
            </div>
        {% endblock %}
        {% extends 'SoccerApp/SoccerApp_base.html' %}

        {% load staticfiles %}
        {% block templatecontent %}
        <div class="admin_panel">
            <form method="POST" id="thisForm" action="../TeamDetail/">
                <div class="frmObject_container">

                    {% csrf_token %}
                    {{ form.non_field_errors }}
                    {{ form.as_table }}

                <div class="frmBtn_container">
                    <input type="submit">

                    <a href="../{{ form.pk }}TeamDelete/"><button id="btn" type="button" >DELETE</button></a>
                       <a href="{% url 'SoccerTeam'%}"> <button id="btn" type="button" >Cancel</button></a>
                    </div>
                </div>

            </form>
        </div>
        {% endblock %}
        
        {% extends 'SoccerApp/SoccerApp_base.html' %}

        {% load staticfiles %}
        {% block templatecontent %}
        <div class="admin_panel">
            <form method="POST" id="thisForm" action="../TournamentDetail/">
                <div class="frmObject_container">

                    {% csrf_token %}
                    {{ form.non_field_errors }}
                    {{ form.as_table }}

                <div class="frmBtn_container">
                    <input type="submit">

                    <a href="../{{ form.pk }}RefereeDelete/"><button id="btn" type="button" >DELETE</button></a>
                       <a href="{% url 'SoccerTeam'%}"> <button id="btn" type="button" >Cancel</button></a>
                    </div>
                </div>

            </form>
        </div>
        {% endblock %}

        {% extends 'base.html' %}
        {% load static from staticfiles %}


            {% block stylesheets %}
            {{ block.super}}
                <link rel="stylesheet" type="text/css" href="{% static 'SoccerPhotoApp/Soccer_style.css' %}">
            {% endblock %}
            {% block pagetop-css %}cover-Photo{% endblock%}
            {% block title %}Soccer Sports{% endblock %}

            {% block page-title %}Soccer World Cup{% endblock %}
            {% block page-subtitle %}Enjoy world soccer news!{% endblock %}
            {% block button1 %}<a href="{% url 'registerPage' %}" class="contact-btn">Register</a>{% endblock %}
            {% block button2 %}<a href="{% url 'SoccerTeam' %}" class="contact-btn">Teams</a>{% endblock %}
            {% block button3 %}<a href="{% url 'DetailsPage' %}" class="contact-btn">Details</a>{% endblock %}

        {% block appcontent %}
             {% block templatecontent %}{% endblock %}
        {% endblock %}
        
        {% extends 'SoccerApp/SoccerApp_base.html' %}
          {% load staticfiles %}
          {% block templatecontent %}
          <div class="admin_panel">
           <h1> Players</h1>
          <table class="table table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Player Name</th>
                <th scope="col">Player Address</th>
                <th scope="col">Player Phone</th>
                  <th scope="col">Player Email</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                  {% for player in players %}
                <th scope="row"></th>
                <td>
                    <ul>
                        <li>{{ player.PlayerName }}</li>
                    </ul>
                </td>
                <td>
                    <ul>
                        <li>{{ player.PlayerAddress}}</li>
                    </ul>
                </td>
                <td>
                    <ul>
                        <li>{{ player.PlayerPhoneNumber }}</li>
                    </ul>
                </td>
                  <td>
                    <ul>
                        <li>{{ player.PlayerEmailAddress }}</li>

                    </ul>
                </td>
                   <td>
                           <a href="./{{player.pk}}/PlayerDetail/"><button id="btn" type="button"  >Details</button></a>
                   </td>
              </tr>
          {% endfor %}

            </tbody>
          </table>
          <!-- Soccer Teams Table-->
              <h1> Teams</h1>
              <table class="table table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Team Name</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                   {% for team in teams %}
                <th scope="row"></th>

                <td>
                    <ul>
                        <li>{{ team.TeamName }}</li>

                    </ul>
                </td>
                  <td>
                      <a href="./{{team.pk}}/TeamDetail/"><button id="btn" type="button"  >Details</button></a>
                  </td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
          <!-- Coaches Table -->
              <h1> Coaches</h1>
          <table class="table table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Coach Name</th>
                <th scope="col">Coach Address</th>
                <th scope="col">Coach Phone</th>
                  <th scope="col">Coach  Email</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                  {% for coach in coaches %}
                <th scope="row"></th>
                <td>
                    <ul>
                        <li>{{ coach.CoachName }}</li>
                    </ul>
                </td>
                <td>
                    <ul>
                        <li>{{ coach.CoachAddress }}</li>
                    </ul>
                </td>
                <td>
                    <ul>
                        <li>{{ coach.CoachPhoneNumber }}</li>

                    </ul>
                </td>
                  <td>
                    <ul>
                        <li>{{ coach.CoachEmailAddress }}</li>
                    </ul>
                </td>
               <td>
                    <a href="./{{coach.pk}}/CoachDetail/"><button id="btn" type="button"  >Details</button></a>
               </td>

            </tbody>
              {% endfor %}
          </table>

          <!-- Referees Table-->
              <h1> Referees</h1>
          <table class="table table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Referee Name</th>
                <th scope="col">Referee Address</th>
                <th scope="col">Referee Phone</th>
                  <th scope="col">Referee  Email</th>
                  <th scope="col">Referee  Kind</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                   {% for referee in referees %}
                <th scope="row"></th>
                <td>
                    <ul>
                        <li>{{ referee.RefereeName }}</li>
                    </ul>
                </td>
                <td>
                    <ul>
                        <li>{{ referee.RefereeAddress }}</li>

                    </ul>
                </td>
                <td>
                    <ul>
                        <li>{{ referee.RefereePhoneNumber }}</li>
                    </ul>
                </td>
                  <td>
                    <ul>
                        <li>{{ referee.RefereeEmailAddress }}</li>
                    </ul>
                </td>
                  <td>
                    <ul>
                        <li>{{ referee.RefereeKind }}</li>
                    </ul>
                </td>
                  <td>
                    <a href="./{{referee.pk}}/RefereeDetail/"><button id="btn" type="button"  >Details</button></a>
                </td>
              </tr>

            {% endfor %}
            </tbody>
          </table>
              <!-- Tournament Table -->
          <h1> Tournaments </h1>
          <table class="table table">
            <thead>
              <tr>
                <th scope="col">#</th>
                  <th scope="col">Tournament Address</th>
                <th scope="col">Tournament Date</th>
                  <th scope="col">Tournament  Time</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                  {% for so in soccer %}
                <th scope="row"></th>
                <td>
                    <ul>
                        <li>{{ so.MatchAddress }}</li>
                    </ul>
                </td>
                <td>
                    <ul>
                        <li>{{ so.MatchDate }}</li>
                    </ul>
                </td>
                <td>
                    <ul>
                        <li>{{ so.MatchTime }}</li>
                    </ul>
                </td>
                  <td>
                    <a href="./{{so.pk}}/TournamentDetail/"><button id="btn" type="button"  >Details</button></a>
                 </td>
              </tr>
            {% endfor %}
            </tbody>
          </table>
          </div>
          {% endblock %}
        
        {% extends 'SoccerApp/SoccerApp_base.html' %}

        {% load staticfiles %}

        {% block templatecontent %}

        <div class="admin_panel">
                <form method="POST" action="{% url 'DetailsPage' %}">

                    <h1>Details Page</h1>
                    <div class="frmBtn_container">
                        <a href="{% url 'TeamDetails' %}"><button type="button" id="btn" >Team Details</button></a>
                    </div>
                </form>
            </div>
        {% endblock %}
        
        {% extends 'SoccerApp/SoccerApp_base.html' %}

        {% load staticfiles %}

        {% block templatecontent %}

        <div class="admin_panel">
                <form method="POST" action="{% url 'registerPage' %}">

                    <h1>Registartion Page</h1>
                    <div class="frmBtn_container">


                        <a href="{% url 'registerForPlayer' %}"><button type="button" id="btn" >Player</button></a>
                        <a href="{% url 'registerForTeam' %}"><button type="button" id="btn" >Team</button></a>
                        <a href="{% url 'registerForCoach' %}"><button type="button" id="btn" >Coach</button></a>
                        <a href="{% url 'registerForReferee' %}"><button type="button"  id="btn" >Referee</button></a>
                        <a href="{% url 'registerForTournament' %}"><button type="button" id="btn" >Tournament</button></a>
                        <a href="{% url 'SoccerTeam' %}"><button type="button" id="btn" value="Cancel">Cancel</button></a>
                    </div>
                </form>
            </div>
        {% endblock %}

    </code>
 <pre>
 
 <p> Jump to:<a href="#code_model">Create a model ,</a><a href="#code_form">Create a forms ,</a><a href="#code_view">Views functions ,</a><a href="#code_url">Urls</a></p>
