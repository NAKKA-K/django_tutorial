from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^polls$', views.IndexView.as_view(), name = 'index'),
  url(r'^polls/(?P<pk>\d+)/$', views.Detail.as_view(), name = 'detail'),
  url(r'^polls/(?P<pk>\d+)/results$', views.ResultsView.as_view(), name = 'results'),
  url(r'^polls/form$', views.FormTest.as_view(), name = 'form'),
]
