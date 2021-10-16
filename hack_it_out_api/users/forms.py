from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import model_to_dict, ModelForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)