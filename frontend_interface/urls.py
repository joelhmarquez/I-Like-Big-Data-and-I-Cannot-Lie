from django.conf.urls import url

from . import views
from .views import HomePageView, TeamPageView, TechnologiesPageView

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name='index'),
	url(r'^about$', TeamPageView.as_view(), name='team'),
	url(r'^tech$', TechnologiesPageView.as_view(), name='tech'),
	url(r'api/map$', views.mapsData, name='mapsData'),
]
