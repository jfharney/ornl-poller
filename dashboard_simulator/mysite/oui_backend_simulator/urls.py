from django.conf.urls import url

from oui_backend_simulator.views import UserRunsView

from . import views

urlpatterns = [
  url(r'^$',views.index,name="index"),
  url(r'^about/(?P<wf_id>\w+)/$', UserRunsView.as_view()),
  url(r'^update/$',views.update,name='update')
]
