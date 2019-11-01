from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views as v
from django.contrib.auth import views as auth_views

app_name = 'auth'
urlpatterns = [
    url('', v.login_view, name='index'),
    #url('', v.logout_view, name='logout'),
    url('logout', auth_views.LogoutView.as_view(), name='logout')
]
