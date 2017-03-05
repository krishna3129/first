from django.conf.urls import url, include
from . import views
urlpatterns = patterns('',
 url(r'^hello/', 'myapp.views.hello', name='hello'),

)
