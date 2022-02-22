from itertools import product
from unicodedata import name
from django.shortcuts import render

# Create your views here.
from movies.models import Film 
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render

class SearchResultsListView(ListView):
    model = filmcontext_object_name = 'film_list'
    template_name = 'search.html'

def get_queryset(self):
    query = selfrequest.GET.get('q')
    return Film.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

def get_context_data(self, **kwargs):
    context = super(SearchResultsListView, self).get_context_data(**kwargs)
    context['query'] = self.request.GET.get('q')
    return context
    