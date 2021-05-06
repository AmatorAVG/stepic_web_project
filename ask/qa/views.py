from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import QuestionManager, Question, Answer
from django.urls import reverse
from django.views import generic

from django.core.paginator import Paginator

def QuestionView(request, id):
    question = get_object_or_404(Question, pk=id)
    answer_set = question.answer_set
    return render(request, 'qa/detail.html', {
        'question': question,
        'answer_set': answer_set,
    })



def NewView(request):
    posts = Question.objects.new()
    limit = request.GET.get('limit', 2)
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
    limit = request.GET.get('limit', 2)
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
