from django.conf.urls import patterns, url
from trackr.views import ItemsView

urlpatterns = patterns('',
	url(r'^items/$', ItemsView.as_view()),
)
