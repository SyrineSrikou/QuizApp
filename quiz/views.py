from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Quiz
from django.core.paginator import Paginator

lst = []
answers = Question.objects.all()
anslist = []


for i in reversed(answers):
    anslist.append(i.answer)

        
def quiz(request):
    questions = Question.objects.all()
    count = Question.objects.all().count()
    paginator = Paginator(questions,1)
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):
        
        questions=paginator.page(paginator.num_pages)
            
    return render(request,'quiz.html',{'questions':questions,'count':count})


def result(request):
    score = 0
    for i in range(len(lst)):
        if lst[i] == anslist[i]:
            score +=1
    return render(request,'result.html',{'score':score,'lst':lst})
        
def saveans(request):
    ans = request.GET['ans']
    lst.append(ans)
        
def welcome(request):
    quizes = Quiz.objects.all().filter(is_active=True)
    lst.clear()
    return render(request,'welcome.html', {'quizes': quizes} )
      
    