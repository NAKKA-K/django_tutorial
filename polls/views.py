from django.shortcuts import render, get_object_or_404, redirect
from .forms import MyForm, VoteForm
from .models import Question, Choice
from django.views import generic
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

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


class FormTest(FormView):
  form_class =MyForm
  template_name = 'form.html'
  success_url = reverse_lazy('polls:index')

form_test = FormTest.as_view() # FormTestクラスからviewを作成


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
