import django.http  # HttpResponse, Http404, request
from django.core.paginator import * # Paginator, EmptyPage exception,
from django.shortcuts import render, get_object_or_404
from django.utils import html               # html.escape()
from django.core.exceptions import ObjectDoesNotExist

from qa.models import Question, Answer

def test(_request):
    return django.http.HttpResponse('OK')


def test2(request):
    post = Question.objects.get(pk=1)
    
    return render(request, '1.html', {
        'post': post
    })
    
    # return django.http.HttpResponse(f'<html><body>{html.escape(request)}</body></html>')


def question_page(request, num: int):
    question = get_object_or_404(Question, pk=num)
    answers = question.answer_set.all()
    
    return render(request, '1.html', {
        'question': question,
        'answers': answers
    })

def popular_questions(request):
    
    qs = Question.objects.popular()
    
    paginator, page = paginate(request, qs)
    
    return render(request, 'many.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def new_questions(request):
    
    qs = Question.objects.new()
    
    paginator, page = paginate(request, qs)
    
    return render(request, 'many.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if not 0 < limit <= 100:
        limit = 10
    
    try:
        page_num = request.GET.get('page', 1)
    except ValueError:
        raise django.http.Http404
    
    paginator = Paginator(qs, limit)
    
    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    query_dict = request.GET.copy()
    if 'limit' in query_dict:
        query_dict['limit'] = limit
    query_dict.pop('page', None)
    paginator.url_template = ['?page=', '']
    if query_dict:
        paginator.url_template[-1] = '&' + query_dict.urlencode()
    
    return paginator, page