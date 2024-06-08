from django import forms
class check(forms.Form):
    Name=forms.CharField(max_length=20)
    Email=forms.EmailField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)