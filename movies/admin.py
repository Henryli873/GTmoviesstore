from django.contrib import admin

# Register your models here.
from .models import Movie, Review, Rating
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'stars', 'date']
    list_filter = ['stars', 'date']
    search_fields = ['movie__name', 'user__username']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Rating, RatingAdmin)