from django import forms
from django.db import models
from .models import Question, Answer

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all(), widget=forms.HiddenInput())
    def clean(self):
       pass
    def __init__(self, *args, **kwargs):
        # self._user = user
        super(AnswerForm, self).__init__(*args, **kwargs)


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        # self._user = user
        super(AskForm, self).__init__(*args, **kwargs)

    def clean(self):
        text = self.cleaned_data['text']
        # if not text.is_valid():
        #    raise forms.ValidationError('question text is wrong', code=12)
        return text

    """def save(self):
        #question = Question(**self.cleaned_data)
        #question.author_id = 1
        #self.cleaned_data['author'] = self._user
        #question.save()
        #return question
        self.cleaned_data['author'] = self._user
        return Question.objects.create(**self.cleaned_data)"""