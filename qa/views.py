from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404

from qa.models import *
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import *


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def do_login(request):
    errors = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                sessionid = request.session.session_key
                response = redirect('home')
                response.set_cookie('sessionid', sessionid,
                                    httponly=True,
                                    expires=datetime.now() + timedelta(days=3)
                                    )
                return response
            else:
                errors.append('Login error: incorrect Username or password.')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', context={'form': form, 'errors': errors})


def signup(request):
    errors = []
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=form.cleaned_data['username']).exists():
                user = form.save()
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                login(request, user)
                sessionid = request.session.session_key
                response = redirect('home')
                response.set_cookie('sessionid', sessionid,
                                    httponly=True,
                                    expires=datetime.now() + timedelta(days=3)
                                    )
                return response
            else:
                errors.append('Error. User with entered name is already exists. '
                              'Please enter different username.')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', context={'form': form, 'errors': errors})


#@login_required
def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return redirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def page_not_found_view(request, exception):
    return render(request, 'qa/404.html', status=200)


def popular(request, *args, **kwargs):
    qts = Question.objects.popular()
    page_obj = paginate(request, qts)
    return render(request, 'qa/new.html', {
        'questions': page_obj.object_list,
        'page_obj': page_obj,
        'title': 'List of popular questions',
    })


def question_details(request, q_id=1):
    try:
        q = int(q_id)
    except TypeError:
        raise Http404()
    try:
        question = Question.objects.get(pk=q)
    except ObjectDoesNotExist:
        raise Http404()

    if request.method == 'POST':
#        form = AnswerForm(request.POST, question=question)
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form._question = question
            answer = form.save()
            messages.success(request, 'Answer added successfully.')
            return redirect(request.path)
    else:
        form = AnswerForm()
#        form = AnswerForm(question=question)
    answers = Answer.objects.filter(question=question).order_by('-added_at')
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })


def new(request, *args, **kwargs):
    qts = Question.objects.new()
    page_obj = paginate(request, qts)
    return render(request, 'qa/new.html', {
        'questions': page_obj.object_list,
        'page_obj': page_obj,
        'title': 'List of recent questions',
    })


def paginate(request, qset):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 100

    try:
        page_number = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404()
    paginator = Paginator(qset, limit)
    try:
        page_obj = paginator.page(page_number)
    except:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj


def scrap(request, *args, **kwargs):
    import requests
    from bs4 import BeautifulSoup
    import re

    # res = requests.get('https://parade.com/1025605/marynliles/trick-questions/')

    with open(
            '/home/mit/Documents/125 Trick Questions (with Answers) That Are Confusing - Parade Entertainment, Recipes, Health, Life, Holidays.html') as file:
        content = file.read()
    html = BeautifulSoup(content, 'html.parser')
    qts = html.select('p')
    questions = []
    answers = []
    for q in qts:
        try:
            res = re.match(r'^\d+\.', q.string)
            if res:
                text = re.sub(r'^\d+\.\s', '', q.string)
                if len(text) > 50:
                    title = text[:50] + '...'
                else:
                    title = text
                quest = Question(title=title, text=text, author=request.user)
                # quest.save()
                questions.append(quest)
                ans = Answer(text=qts[qts.index(q) + 1].string, question=quest, author=request.user)
                # ans.save()
                answers.append(ans)
        except TypeError:
            continue

    return render(request, 'qa/new1.html', context={'questions': zip(questions, answers)})
