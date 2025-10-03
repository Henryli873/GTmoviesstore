from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Petition, Vote
from .forms import PetitionForm

def petition_list(request):
    petitions = Petition.objects.all().order_by('-created_at')
    return render(request, 'petitions/petition_list.html', {'petitions': petitions})

@login_required
def petition_create(request):
    if request.method == "POST":
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            return redirect('petition_list')
    else:
        form = PetitionForm()
    return render(request, 'petitions/petition_create.html', {'form': form})

@login_required
def petition_vote(request, petition_id, vote_type):
    petition = get_object_or_404(Petition, id=petition_id)
    value = True if vote_type == 'yes' else False
    vote, created = Vote.objects.update_or_create(
        petition=petition,
        user=request.user,
        defaults={'value': value}
    )
    return redirect('petition_list')