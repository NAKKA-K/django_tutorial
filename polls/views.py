from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import MyForm
from .models import Question, Choice

# Create your views here.

def vote(request, pk):
  question = get_object_or_404(Question, pk = pk)

  try:
    selected_choice = question.choice_set.get(pk = request.POST['choice'])

  except(KeyError, Choice.DoesNotExist):
    return render(request, 'detail.html', {
      'question': question,
      'error_message': 'You did not select a choice',
    })

  else:
    selected_choice.votes += 1
    selected_choice.save()
    return redirect('polls:results', pk)


def results(request, pk):
  obj = get_object_or_404(Question, pk = pk)
  return render(request, 'results.html', {
    'question': obj,
  })


def form_test(request):
  form = MyForm()
  return render(request, 'form.html', {
    'form': form,
  })


class IndexView(generic.ListView):
  template_name = 'index.html'
  context_object_name = 'questions'
  #queryset = Question.objects.all() #get_queryset()をオーバーライドするか、querysetを変更するか

  def get_queryset(self):
    return Question.objects.all()


class DetailView(generic.DetailView):
  template_name = 'detail.html'
  model = Question


class ResultsView(generic.DetailView):
  template_name = 'results.html'
  model = Question
