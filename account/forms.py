from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'first_name', 'email']

    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Passwords doesn\'t match')
        return cd['password2']