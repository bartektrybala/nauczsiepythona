from django import forms

from .models import UserApproach, Code



class ApproachForm(forms.ModelForm):
    class Meta:

        model = UserApproach
        fields = ['user_approach']
        labels = {'user_approach': ''}
        widgets = {'user_approach': forms.Textarea(attrs={
            'cols': 100,
            'id': 'editor',
        })}


class UserCode(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['test_code']
        labels = {'test_code': ''}
        widgets = {'test_code': forms.Textarea(attrs={
            'cols': 100,
            'id': 'code',
        })}
