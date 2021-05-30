from django import forms
from django.db import models
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    # def __init__(self, *args, **kwargs):
    #     # self._user = user
    #     super(AskForm, self).__init__(*args, **kwargs)

    def clean(self):
        pass
        # text = self.cleaned_data['text']
        # # if not text.is_valid():
        # #    raise forms.ValidationError('question text is wrong', code=12)
        # return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    # question = forms.ModelChoiceField(queryset=Question.objects.all(), widget=forms.HiddenInput())
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean(self):
       pass
    # def __init__(self, *args, **kwargs):
    #     # self._user = user
    #     super(AnswerForm, self).__init__(*args, **kwargs)

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer