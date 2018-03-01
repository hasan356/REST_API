from django.conf.urls import url,include

from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserCreateView,UserLoginView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^register/$', UserCreateView.as_view(), name='register'),#user_registration_url
    url(r'^login/$', UserLoginView.as_view(), name='login'),#login_url
]
urlpatterns = format_suffix_patterns(urlpatterns)