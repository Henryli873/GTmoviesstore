from django.db import models
from movies.models import Movie
from accounts.models import Profile

# Create your models here.

def get_top_movies_by_continent(continent):
    """
    Returns the top 3 movies purchased by users from the given continent.
    """
    # Get all users from the continent
    profiles = Profile.objects.filter(continent=continent)
    user_ids = profiles.values_list('user_id', flat=True)

    # Get orders from those users
    from cart.models import Order, Item
    orders = Order.objects.filter(user_id__in=user_ids)
    order_ids = orders.values_list('id', flat=True)

    # Aggregate purchases by movie
    from django.db.models import Sum
    movie_purchases = Item.objects.filter(order_id__in=order_ids).values('movie').annotate(
        total_purchases=Sum('quantity')
    ).order_by('-total_purchases')[:3]

    # Get the movie objects and create list with continent-specific counts
    result = []
    for mp in movie_purchases:
        movie = Movie.objects.get(id=mp['movie'])
        result.append({
            'name': movie.name,
            'purchase_count': mp['total_purchases']
        })

    return result
