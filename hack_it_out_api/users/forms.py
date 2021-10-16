from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import model_to_dict, ModelForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)