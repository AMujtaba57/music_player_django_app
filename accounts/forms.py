from django.forms import ModelForm
from .models import RegistrationUser


class RegisterForm(ModelForm):
    class Meta:
        model = RegistrationUser
        fields = ['email', 'password', 'first_name', 'last_name']