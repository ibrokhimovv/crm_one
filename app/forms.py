from django import forms

class LeadForm(forms.Form):
    name = forms.CharField(max_length=20)
    sourname = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0)