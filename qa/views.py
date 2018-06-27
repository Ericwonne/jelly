from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import Question,Answer
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from user.models import Userinfo
from django.contrib.auth import SESSION_KEY
import json

class QACenterView(ListView):
    model=Question

    template_name = "qa/qa_center.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

def ask(request):
    title=request.POST['title']
    content=request.POST['content']
    categories=request.POST['categories']
    asker=request.session.get(SESSION_KEY)
    question=Question.objects.create(title=title,content=content,categories=categories,asker_id=asker)
    return HttpResponseRedirect('/qa/Q_detail/'+str(question.id)+'/')

def answer(request):
    """
    对问题的回答

    :param request:
    :return:
    """
    content=request.POST['content']
    # question_id=request.GET['question_id']
    question_id=26
    answerer=request.session.get(SESSION_KEY)
    answer=Answer.objects.create(question_id=question_id,content=content,answerer_id=answerer)
    return HttpResponseRedirect('/qa/A_detail/'+str(answer.pk)+'/')

class QuestionDetail(DetailView):
    """
    继承自DetailView，提供get_object函数（自动寻找并利用请求的url中携带的pk或slug参数，
    得到对应的模型对象），并默认寻求'<modelname>_detail.html'模板
    """
    model=Question

    def get_context_data(self, **kwargs):
        context=super(QuestionDetail,self).get_context_data(**kwargs)
        question=self.get_object()
        context['user']=question.asker
        return context

class AnswerDetail(DetailView):
    """
    继承自DetailView，提供get_object函数（自动寻找并利用请求的url中携带的pk或slug参数，
    得到对应的模型对象），并默认寻求'<modelname>_detail.html'模板
    """
    model=Answer

    def get_context_data(self, **kwargs):
        context=super(AnswerDetail,self).get_context_data(**kwargs)
        answer=self.get_object()
        context['user']=answer.answerer
        return context