from django.shortcuts import render, get_object_or_404, get_list_or_404
from myfantasy.models import Player, Team
from django import forms
from myfantasy.forms import *
import json
from django.http.response import HttpResponse
# Create your views here.

text = []
myteam = []

def test(request):

    if request.method == 'POST' and request.is_ajax():
        form = TestForm(request.POST)
        if form.is_valid():
            if text.count(form.cleaned_data['test_name']) == 0: text.append(form.cleaned_data['test_name'])
    else:
        form = TestForm()
        if len(text)==0: text.append("before")
    return render(request, 'myfantasy/test.html', {'form': form, 'text': text})

def index(request):
    if request.method == 'POST' and request.is_ajax():
        form = TeamForm(request.POST)
        if form.is_valid():
            if myteam.count(form.cleaned_data['pid']) == 0:
                myteam.append(form.cleaned_data['pid'])
    else:
        form = TeamForm()
    players = Player.objects.all()
    return render(request, 'myfantasy/index.html', {'players' : players, 'myteam': myteam})

def player_details(request, player_id):
    player = get_object_or_404(Player, pk = player_id)
    return render(request, 'myfantasy/player.html', {'player' : player})

def team_details(request, team_id):
    team = get_object_or_404(Team, pk = team_id)
    players = Player.objects.all().filter(team = team_id).order_by('position')
    #return render(request, 'myfantasy/test2.html', {'team': team, 'players': players})
    return render(request, 'myfantasy/team.html', {'team' : team, 'players': players})
