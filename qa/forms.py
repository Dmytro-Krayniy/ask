from django import forms
from .models import Question, Answer, User


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        title = self.cleaned_data['text']
        if len(title) > 50:
            self.title = title[:50] + '...'
        return self.cleaned_data

    def save(self, commit=True):
        question = Question(author=User.objects.get(pk=1), **self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(min_length=2, widget=forms.Textarea(attrs={'rows': 3, 'cols': 80}))
    question = forms.ModelChoiceField(queryset=Question.objects, to_field_name='title')

    def __init__(self, *args, **kwargs):  #(self, *args, question=Question.objects.filter(pk=1), **kwargs)
        super().__init__(*args, **kwargs)
        #self.fields['question'].initial = question

    def clean(self):
        st = self.cleaned_data['text']
        if len(st.strip()) < 3:
            raise forms.ValidationError('Answer is incorrect. Answers minimum length should be 3 characters')
        return self.cleaned_data

    def save(self, commit=True):
        answer = Answer(**self.cleaned_data)
        answer.author = User.objects.get(pk=1)
        answer.save()
        return answer

