from django.shortcuts import render
from .models import get_top_movies_by_continent
from django.http import JsonResponse

def index(request):
    template_data = {}
    template_data['title'] = 'Trend Map'
    return render(request, 'trendmap/trendmap.html', {'template_data': template_data})

def get_trending_movies(request, continent):
    movies = get_top_movies_by_continent(continent)
    return JsonResponse({'movies': movies})
