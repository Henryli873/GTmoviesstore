from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    continent = models.CharField(
        max_length=20,
        choices=[
            ('North America', 'North America'),
            ('South America', 'South America'),
            ('Europe', 'Europe'),
            ('Africa', 'Africa'),
            ('Asia', 'Asia'),
            ('Australia', 'Australia'),
            ('Antarctica', 'Antarctica'),
        ],
        default='North America'
    )

    def __str__(self):
        return f'{self.user.username} - {self.continent}'
