import django.http  # HttpResponse, Http404, request
from django.core.paginator import * # Paginator, EmptyPage exception,
from django.shortcuts import render
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
    try:
        post = Question.objects.get(pk=num)
    except ObjectDoesNotExist:
        raise django.http.Http404
    
    return render(request, '1.html', {
        'post': post
    })
    pass

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
        limit = int(request.GET.get('limit', 4))
    except ValueError:
        limit = 4
    if not 0 < limit <= 100:
        limit = 4
    
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
    query_dict.pop('page')
    paginator.url_template = ['?page=', '']
    if query_dict:
        paginator.url_template[-1] = '&' + query_dict.urlencode()
    
    return paginator, page