from django import forms
from .models import Question, Answer, User
from django.core.exceptions import ValidationError


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

    def clean(self):
        return self.cleaned_data


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'})
        }

    def save(self):
        user = User(**self.cleaned_data)
        user.set_password(self.cleaned_data['password'])
        user.save()
        #self.save_m2m()  # execute only if model has relations many-to-many
        return user


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        title = self.cleaned_data['text']
        if len(title) > 50:
            self.title = title[:50] + '...'
        return self.cleaned_data

    def save(self, commit=True):
        question = Question(author=self._user, **self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(min_length=1, widget=forms.Textarea(attrs={'rows': 3, 'cols': 80}))
#    question = forms.ModelChoiceField(queryset=Question.objects, to_field_name='title')

    def clean(self):
        st = self.cleaned_data['text']
        if len(st.strip()) < 3:
            raise forms.ValidationError('Answer is incorrect. Answers minimum length should be 3 characters')
        return self.cleaned_data

    def save(self, commit=True):
        answer = Answer(**self.cleaned_data)
        answer.author = self._user
        answer.question = self._question
        answer.save()
        return answer

