from django.conf.urls import url

from . import views
from .views import HomePageView, TeamPageView, TechnologiesPageView, AnalyticsPageView

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name='index'),
	url(r'^team$', TeamPageView.as_view(), name='team'),
	url(r'^tech$', TechnologiesPageView.as_view(), name='tech'),
	url(r'^analytics$', AnalyticsPageView.as_view(), name='analytics'),
	url(r'api/map$', views.mapsData, name='mapsData'),
	url(r'^api/data/(?P<statename>\w{0,50})$', views.stateData, name='stateData'),
]
