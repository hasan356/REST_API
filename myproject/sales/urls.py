from django.conf.urls import url

from django.contrib import admin

from .views import crudview,createview

urlpatterns = [
    url(r'^$', createview.as_view() , name='createview'),
    url(r'^(?P<pk>\d+)/$', crudview.as_view() , name='crudview'),
]
