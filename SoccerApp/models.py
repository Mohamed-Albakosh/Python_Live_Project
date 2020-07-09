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

    SoccerMatchOB = models.Manager()
