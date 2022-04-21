from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Profile

EDUCATION_CHOICES = (
    ('1', 'Primary School'),
    ('2', 'High School'),
    ('3', 'University'),
    ('4', 'College'),
)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'inputUsername'}
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'type': 'password',
               'class': 'form-control',
               'id': 'inputPassword1'}
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'type': 'password',
               'class': 'form-control',
               'id': 'inputPassword2'}
    ))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class EditProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control-file',
               'id': 'inputProfileimage',
               'type': 'file'}
    ))

    class Meta:
        model = Profile
        fields = ['profile_image']
