# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Subject, SubCategory
# Create your views here.
def index(request):
    context = {'categories': 'hello world'}
    return render(request, 'airtraining/index.html', context)

def quizpage(request):
    questionquery = Question.objects.all()[:5]
    page = request.GET.get('page', 1)
    p = Paginator(questionquery, 1)
    questions = p.page(page)
    print(list(p.page(1).object_list))
    subjects = Subject.objects.all()
    subcategories = SubCategory.objects.all()
    print(questions.has_other_pages)
    context = {'questions': questions, 'subjects': subjects, 'subcategories': subcategories}
    if request.method == 'POST':
        if form.is_valid():
            # Need to check if passwords match and then create new user
            print(form.cleaned_data['option'])

            
    return render(request, 'airtraining/quizpage.html', context)
