from django.urls import path
from . import views as v

app_name = 'market'
urlpatterns = [
    path('market', v.market_main_view, name='market_main'),
    path('update', v.update_inventory, name='update_inventory'),
    path('my_inventory', v.get_user_inventory, name='my_inventory'),
]
