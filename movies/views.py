from django.shortcuts import render, get_object_or_404
from .models import Genre, Film
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, InvalidPage

class FilmGenre(ListView):
    model = Film

    def get(self,request, genre_id=None):
        genre = None
        films = None
        if genre_id != None:
            genre = get_object_or_404(Genre, id = genre_id)
            films = Film.objects.filter(genre = genre, available = True)
        else:
            films = Film.objects.all().filter(available = True)

        '''Pagination code'''
        paginator = Paginator(films, 6)
        try:
            page = int(request.Get.get('page', '1'))
        except:
            page = 1
        try:
            films = paginator.page(page)
        except (EmptyPage, InvalidPage):
            films = paginator.page(paginator.num_pages)

        return render(request,"movies/genre.html",{'genre':genre, 'films':films})

        





class FilmDetail(DetailView):
    model = Film

    def get(self,request, genre_id, film_id):
        try:
            film = Film.objects.get(genre_id = genre_id, id = film_id)
        except Exception as e:
            raise e
        return render(request, "movies/film.html",{'film':film})
# Create your views here.
