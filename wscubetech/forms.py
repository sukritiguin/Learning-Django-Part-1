from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)