from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Petition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="petitions")
    created_at = models.DateTimeField(auto_now_add=True)

    def yes_votes(self):
        return self.votes.filter(value=True).count()

    def no_votes(self):
        return self.votes.filter(value=False).count()

    def __str__(self):
        return self.title
    
class Vote(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.BooleanField()  # True = Yes, False = No

    class Meta:
        unique_together = ('petition', 'user')  # Prevent double voting

    def __str__(self):
        return f"{self.user.username} voted {'Yes' if self.value else 'No'}"