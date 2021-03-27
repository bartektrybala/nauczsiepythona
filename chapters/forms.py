from django import forms

from .models import Topic, UserApproach


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['approach']
        labels = {'approach': ''}
        widgets = {'approach': forms.Textarea(attrs={'cols': 80})}


class ApproachForm(forms.ModelForm):
    class Meta:
        model = UserApproach
        fields = ['user_approach']
        labels = {'user_approach': ''}
        widgets = {'user_approach': forms.Textarea(attrs={'cols': 80})}
