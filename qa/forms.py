from django import forms
from .models import Question, Answer, User


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        title = self.cleaned_data['text']
        if len(title) > 50:
            self.title = title[:50] + '...'

    def save(self, commit=True):
        question = Question(**self.cleaned_data, author=User.objects.get(pk=1))
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 80}))

    def save(self, commit=True):
        answer = Answer(**self.cleaned_data)
        return answer

