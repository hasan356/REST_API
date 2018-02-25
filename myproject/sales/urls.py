from django.conf.urls import url,include

from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from .views import crudview,createview,UserView,UserDetailsView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', # ADD THIS URL
                               namespace='rest_framework')),
    url(r'^$', createview.as_view() , name='createview'),
    url(r'^itemslists/(?P<pk>[0-9]+)/$', crudview.as_view() , name='crudview'),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token), # Add this line
]

urlpatterns = format_suffix_patterns(urlpatterns)