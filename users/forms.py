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
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'inputFirstname'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'inputLastname'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'inputEmail'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']


class EditUserForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control bg-light text-dark',
               'id': 'inputFirstname'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control bg-light text-dark',
               'id': 'inputLastname'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control bg-light text-dark',
               'id': 'inputEmail'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EditProfileForm(forms.ModelForm):
    age = forms.CharField(widget=forms.NumberInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'inputAge'}))
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control',
               'id': 'inputEducation'}))
    profile_image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control-file',
               'id': 'inputProfileimage',
               'type': 'file'}
    ))

    class Meta:
        model = Profile
        fields = ['age', 'education', 'profile_image']



