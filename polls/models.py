import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
  class Meta:
    verbose_name = '質問'
    verbose_name_plural = 'questions'
    ordering = ['-published_date']

  question_text = models.CharField(max_length=200)
  published_date = models.DateTimeField('date published')

  def was_published_recently(self):
    return timezone.now() >= self.published_date >= timezone.now() - datetime.timedelta(days = 1)

  def what_days_ago(self):
    days_ago = (timezone.now() - self.published_date) / datetime.timedelta(days=1)
    return str(int(days_ago)) + '日前'

  what_days_ago.admin_order_field = 'published_date' # 並び替えの対象カラム

  def __str__(self):
    return self.question_text



class Choice(models.Model):
  question = models.ForeignKey(Question)
  choice_txt = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_txt

