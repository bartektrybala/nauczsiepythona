from django import forms

from .models import UserApproach


class ApproachForm(forms.ModelForm):
    class Meta:

        model = UserApproach
        fields = ['user_approach']
        labels = {'user_approach': ''}
        widgets = {'user_approach': forms.Textarea(attrs={
            'cols': 100,
            'id': 'editor',
        })}

