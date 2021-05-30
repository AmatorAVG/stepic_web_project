from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import QuestionManager, Question, Answer
from django.urls import reverse
from django.views import generic
from qa.forms import AskForm, AnswerForm

from django.core.paginator import Paginator

def question_add(request):

    if request.method == "POST":
        # form = AskForm(request.user, request.POST)
        form = AskForm(request.POST)
        if form.is_valid():
            # form_title = form.data['title']
            # form_text = form.data['text']
            # saving_all = Question.objects.create(title=form_title, text=form_text, author_id=1)
            # url = saving_all.get_url()
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/question_add.html', {'form': form, 'question_id': 1})


def QuestionView(request, id):

    question = get_object_or_404(Question, pk=id)
    answer_set = question.answer_set
    if request.method == "POST":

        form = AnswerForm(request.POST)
        # form_text = form.data['text']
        # saving_all = Answer.objects.create(question=question, text=form_text, author_id=1)
        if form.is_valid():
            form._user = request.user
            _ = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)

        # return render(request, 'qa/detail.html', {
        # 'question': question,
        # 'answer_set': answer_set, 'form': form
        # })
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(request, 'qa/detail.html', {'question': question,
        'answer_set': answer_set, 'form': form, 'question_id': question.id})

def NewView(request):
    posts = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)  # Page
    return render(request, 'qa/new.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })

def PopularView(request):
    posts = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)  # Page
    return render(request, 'qa/popular.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })




def test(request, *args, **kwargs):
    return HttpResponse('OK')
# Create your views here.
