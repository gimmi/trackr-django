from django.conf.urls import patterns, url
from trackr import views

urlpatterns = patterns('',
    url(r'^items/$', views.ItemsView.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/$', views.ItemView.as_view()),
    url(r'^tags/$', views.TagsView.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagView.as_view()),
    url(r'^items/(?P<item_id>[0-9]+)/comments/$', views.CommentsView.as_view()),
    url(r'^items/(?P<item_id>[0-9]+)/comments/(?P<pk>[0-9]+)/$', views.CommentView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserView.as_view()),
)
