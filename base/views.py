from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from base.models import Question


def index(request):
    questions = Question.objects.all()[:5]
    context = {
        'questions': questions
    }
    return render(request, 'questions/index.html', context=context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(f'Here is the question with id "{question_id}": {question} ')
