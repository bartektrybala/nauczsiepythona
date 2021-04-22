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
    email = forms.EmailField()
    age = forms.IntegerField()
    education = forms.ChoiceField(choices=EDUCATION_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'age', 'education']


class EditUserForm(UserChangeForm):
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
        fields = ['first_name', 'last_name', 'email']


class EditProfileForm(forms.ModelForm):
    age = forms.CharField(widget=forms.NumberInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'inputAge'}))
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control',
               'id': 'inputEducation'}))
    profile_image = forms.ImageField()

    class Meta:
        model = Profile
        exclude = ('password',)
        fields = ['age', 'education', 'profile_image']



