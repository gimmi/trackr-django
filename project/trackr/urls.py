from django.conf.urls import patterns, url
from trackr.views import ItemsView, ItemView

urlpatterns = patterns('',
	url(r'^items/$', ItemsView.as_view()),
	url(r'^items/(?P<pk>[0-9]+)/$', ItemView.as_view()),

)
