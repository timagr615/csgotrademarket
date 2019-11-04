from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views as v
from django.contrib.auth import views as auth_views

app_name = 'auth'
urlpatterns = [
    url('logout', v.logout_view, name='logout'),
    url('', v.login_view, name='authPage'),
]
