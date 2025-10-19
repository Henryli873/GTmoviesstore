from django.urls import path
from . import views

app_name = "trendmap"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/trending/<str:continent>/", views.get_trending_movies, name="get_trending_movies"),
]
