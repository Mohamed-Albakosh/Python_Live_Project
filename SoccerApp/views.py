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
