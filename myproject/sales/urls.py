from django.conf.urls import url,include

from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from .views import SalesCreateView,SalesDetailView,SalesUpdateView,SalesListView,SalesDeleteView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', # ADD THIS URL
                               namespace='rest_framework')),
    url(r'^$', SalesListView.as_view() , name='list'),
    url(r'^itemlists/$', SalesCreateView.as_view(), name='create'),
    url(r'^itemlists/(?P<pk>[0-9]+)/$', SalesDetailView.as_view() , name='detail'),
    url(r'^itemlists/(?P<pk>[0-9]+)/delete/$', SalesDeleteView.as_view() , name='delete'),
    url(r'^itemlists/(?P<pk>[0-9]+)/edit/$', SalesUpdateView.as_view() , name='edit'),
]
urlpatterns = format_suffix_patterns(urlpatterns)