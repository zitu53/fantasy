from django import forms

class TestForm(forms.Form):
    test_name = forms.CharField(label = 'your name', max_length=100)

class TeamForm(forms.Form):
    pid = forms.IntegerField()

