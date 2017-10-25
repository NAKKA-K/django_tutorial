from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .forms import MyForm, VoteForm
from .models import Question, Choice
from django.views import generic
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class Detail(generic.detail.SingleObjectMixin, generic.FormView):
  model = Question # モデルを取得するにはSingleObjectMixinが必要？
  form_class = VoteForm # 形式等、元となるFOrmを指定
  context_object_name = 'question' # templateから呼び出す名前
  template_name = 'detail.html'

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().get(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().post(request, *args, **kwargs)

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['question'] = self.object # get.postで代入したQuestionを追加
    return kwargs

  def form_valid(self, form):
    form.vote() # 成功時に投票する
    return super().form_valid(form)

  def get_success_url(self):
    return resolve_url('polls:results', self.kwargs['pk']) # urlに含まれていたpkをresultsに送る



def results(request, pk):
  obj = get_object_or_404(Question, pk = pk)
  return render(request, 'results.html', {
    'question': obj,
  })


class FormTest(generic.FormView):
  form_class =MyForm
  template_name = 'form.html'
  success_url = reverse_lazy('polls:index')



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
