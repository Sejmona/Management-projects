from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ukol
from .forms import UkolForm

# Seznam úkolů
@login_required
def seznam_ukolu(request):
    ukoly = Ukol.objects.filter(vlastnik=request.user)
    return render(request, 'ukoly/seznam_ukolu.html', {'ukoly': ukoly})

# Přidání úkolu
@login_required
def pridat_ukol(request):
    if request.method == 'POST':
        form = UkolForm(request.POST)
        if form.is_valid():
            ukol = form.save(commit=False)
            ukol.vlastnik = request.user
            ukol.save()
            return redirect('seznam_ukolu')
    else:
        form = UkolForm()
    return render(request, 'ukoly/pridat_ukol.html', {'form': form})

# **Editace úkolu**
@login_required
def edit_ukol(request, pk):
    ukol = get_object_or_404(Ukol, pk=pk, vlastnik=request.user)
    if request.method == 'POST':
        form = UkolForm(request.POST, instance=ukol)
        if form.is_valid():
            form.save()
            return redirect('seznam_ukolu')
    else:
        form = UkolForm(instance=ukol)
    return render(request, 'ukoly/edit_ukol.html', {'form': form})

# Mazání úkolu
@login_required
def smazat_ukol(request, pk):
    ukol = get_object_or_404(Ukol, pk=pk, vlastnik=request.user)
    if request.method == 'POST':
        ukol.delete()
        return redirect('seznam_ukolu')
    return render(request, 'ukoly/smazat_ukol.html', {'ukol': ukol})



