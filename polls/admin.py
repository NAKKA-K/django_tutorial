from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.


#Questionの主キーとリレーションされているので、インラインで入力させるフォームを定義
class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3


class QuestionAdmin(admin.ModelAdmin):
  inlines = [ChoiceInline] #choice入力フォームを反映

  #Questionの入力フォームの見た目変更
  fieldsets = [
    ('Body'     , {'fields': ['question_text']}),
    ('Date info', {'fields': ['published_date']}),
  ]

  list_display = ('question_text', 'published_date', 'what_days_ago') #Questionの項目の見た目変更

  list_filter = ['published_date']
  search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
  list_display = ('choice_txt', 'question', 'votes')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
