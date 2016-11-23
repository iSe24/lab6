from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^books/$', views.books, name='bookexmp'),
    url(r'^books/govorit/(?P<pk>[0-9]+)/$', views.govorit, name='govorit'),
    url(r'^test/$', views.MyView.as_view(),name='test' ),
]
