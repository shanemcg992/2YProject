from django.urls import path
from .views import FilmGenre, FilmDetail

app_name = 'movies'

urlpatterns = [
    path('', FilmGenre.as_view(), name = 'allFilmGenre'),
    path('search/', include('search_app.urls')),
    path('<uuid:genre_id>/', FilmGenre.as_view(), name = 'films_by_genre'),
    path('<uuid:genre_id>/<uuid:film_id>/', FilmDetail.as_view(), name = 'film_detail'),
]