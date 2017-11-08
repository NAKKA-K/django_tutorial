import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class QuestionQuerySet(models.query.QuerySet):
  def is_published(self): # 実装をmodelsですることも可能だが、querysetを拡張したほうが柔軟性のある呼び出しが可能になる
    return self.filter(published_date__lte = timezone.now())

class Question(models.Model):
  class Meta:
    verbose_name = '質問'
    verbose_name_plural = 'questions'
    ordering = ['-published_date']

  question_text = models.CharField(max_length=200)
  published_date = models.DateTimeField('date published')


  objects = models.Manager.from_queryset(QuestionQuerySet)()
  @classmethod
  def get_published_data(cls): # Question.get_published_data()で公開済みのquerysetが取得できる
    return cls.objects.is_published()

  def was_published_recently(self): # 一日中に公開したものか？
    return timezone.now() >= self.published_date >= timezone.now() - datetime.timedelta(days = 1)

  def what_days_ago(self): # 何日前に公開したものか?
    days_ago = (timezone.now() - self.published_date) / datetime.timedelta(days=1)
    return str(int(days_ago)) + '日前'

  what_days_ago.admin_order_field = 'published_date' # 並び替えの対象カラム

  def __str__(self): # これがないと常時されるインスタンスの名前が全てQuestion Objectになる
    return self.question_text



class Choice(models.Model):
  question = models.ForeignKey(Question)
  choice_txt = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_txt

