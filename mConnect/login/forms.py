from django import forms

class log_in(forms.Form):
    username = forms.CharField(label=False, min_length=3, max_length=20, widget=forms.TextInput(attrs={'class':'lg-field', 'placeholder':'Username'}))
    password = forms.CharField(label=False, min_length=6, max_length=20, widget=forms.TextInput(attrs={'class':'lg-field', 'placeholder':'Password', 'type':'password'}))