from django.contrib.auth import get_user_model
from django.forms import forms, ModelForm


class UserUpdateForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
