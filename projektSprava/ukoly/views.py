from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ukol

@login_required
def seznam_ukolu(request):
    ukoly = Ukol.objects.filter(vlastnik=request.user)
    return render(request, 'ukoly/seznam_ukolu.html', {'ukoly': ukoly})

