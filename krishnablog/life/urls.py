from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.life_calender),
  url(r'(?P<life_pk>\d+)/(?P<task_pk>\d+)/$', views.task_detail),
  url(r'(?P<pk>\d+)/$', views.life_tasks),
]
