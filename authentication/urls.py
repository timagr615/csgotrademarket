from django.urls import path
from . import views as v

app_name = 'auth'
urlpatterns = [
    path('logout', v.logout_view, name='logout'),
    path('', v.login_view, name='authPage'),
]
