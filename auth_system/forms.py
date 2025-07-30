from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логін:", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль:", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'