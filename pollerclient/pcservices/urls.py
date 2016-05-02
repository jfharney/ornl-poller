from django.conf.urls import url

from . import views
from pcservices.views import UserRunsView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userruns/(?P<name>\w+)/$', UserRunsView.as_view()),
]