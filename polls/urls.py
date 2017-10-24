from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name = 'index'),
  url(r'^(?P<pk>\d+)/$', views.detail, name = 'detail'),
  url(r'(?P<pk>\d+)/results$', views.ResultsView.as_view(), name = 'results'),
  url(r'^form$', views.form_test, name = 'form'),
]
