from django import forms
from login.models import MyUser


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = MyUser
        fields = '__all__'
