from django.urls import path
from . import views

app_name='watchlist'

urlpatterns = [
    path('add/<uuid:film_id>/', views.add_watchlist, name='add_watchlist'),
    path('', views.watchlist_detail, name='watchlist_detail'),
    path('remove/<uuid:film_id>/', views.watchlist_remove, name='watchlist_remove'),
    path('full_remove/<uuid:film_id>/', views.full_remove, name='full_remove'),
]