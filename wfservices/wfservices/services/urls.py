from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$',views.index,name='index'),
  url(r'service0/$', views.service0, name='service0'),
  url(r'service1/$', views.service1, name='service1'),
  url(r'service2/$', views.service2, name='service2'),
  url(r'service3/$', views.service3, name='service3'),
  url(r'service4/$', views.service4, name='service4'),
  url(r'service5/$', views.service5, name='service5'),
]

