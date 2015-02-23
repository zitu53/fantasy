from django.shortcuts import render, get_object_or_404, get_list_or_404
from myfantasy.models import Player, Team
from django import forms
import json
from django.http.response import HttpResponse
# Create your views here.

text = []

class TestForm(forms.Form):
    test_name = forms.CharField(label = 'your name', max_length=100)

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
    players = Player.objects.all()
    return render(request, 'myfantasy/index.html', {'players' : players})

def player_details(request, player_id):
    player = get_object_or_404(Player, pk = player_id)
    return render(request, 'myfantasy/player.html', {'player' : player})

def team_details(request, team_id):
    team = get_object_or_404(Team, pk = team_id)
    return render(request, 'myfantasy/team.html', {'team' : team})
