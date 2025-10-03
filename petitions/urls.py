from django.urls import path
from . import views

urlpatterns = [
    path('', views.petition_list, name='petition_list'),
    path('create/', views.petition_create, name='petition_create'),
    path('<int:petition_id>/vote/<str:vote_type>/', views.petition_vote, name='petition_vote'),
]