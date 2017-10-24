from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .forms import MyForm, VoteForm
from .models import Question, Choice
from django.views import generic
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class Detail(generic.detail.SingleObjectMixin, generic.FormView):
  model = Question
  form_class = VoteForm
  context_object_name = 'question'
  template_name = 'detail.html'

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().get(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().post(request, *args, **kwargs)

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['question'] = self.object
    return kwargs

  def form_valid(self, form):
    form.vote()
    return super().form_valid(form)

  def get_success_url(self):
    return resolve_url('polls:results', self.kwargs['pk'])

detail = Detail.as_view()


def results(request, pk):
  obj = get_object_or_404(Question, pk = pk)
  return render(request, 'results.html', {
    'question': obj,
  })


class FormTest(generic.FormView):
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
