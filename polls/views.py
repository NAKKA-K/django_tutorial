from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import MyForm, VoteForm
from .models import Question, Choice
from django.views import generic

# Create your views here.

def detail(request, pk):
  obj = get_object_or_404(Question, pk = pk)
  form = VoteForm(question = obj, data = request.POST or None)
  if form.is_valid():
    form.vote()
    return redirect('polls:results', pk)

  return render(request, 'detail.html', {
    'form': form,
    'question':obj,
  })


def results(request, pk):
  obj = get_object_or_404(Question, pk = pk)
  return render(request, 'results.html', {
    'question': obj,
  })


def form_test(request):
  form = MyForm(request.POST or None)
  message = ''
  if form.is_valid():
    message = 'データを送信しました'
  elif request.method != 'GET':
    message = '不正な値です'

  return render(request, 'form.html', {
    'form': form,
    'message': message,
  })


class IndexView(generic.ListView):
  template_name = 'index.html'
  model = Question
  context_object_name = 'questions'


class DetailView(generic.DetailView):
  template_name = 'detail.html'
  model = Question


class ResultsView(generic.DetailView):
  template_name = 'results.html'
  model = Question
