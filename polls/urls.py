from django.urls import path
from django.urls import reverse
from django.urls import reverse_lazy

from django.conf.urls import url

from polls.views import (

    statistics_view,

index3,
)

from . import views
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('index', views.index3, name='index3'),
    #path('', views.get_name, name='get_name'),
    path('head', views.header, name='header'),
    path('about', views.about, name='about'),
    path('xidmet', views.xidmet, name='xidmet'),
    path('contact', views.contact, name='contact'),
    #path('luget', views.dictionary, name='dictionary'),
    path('learn', views.learn, name='learn'),
    path('index2', views.index2, name='index2'),
   # path('static', stat, name='stat'),
    #url(r'^statistics/(?P<statistics_slug>[-\w]+)/$', statistics_view , name='statistics_view'),
   # path('research', views.research, name='research'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', statistics_view, name='statistics_detail'),

]



