from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['approach']
        labels = {'approach': ''}
        widgets = {'approach': forms.Textarea(attrs={'cols': 80})}
