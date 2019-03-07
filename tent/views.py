from django.shortcuts import render, redirect
from tent.forms import OfferForm


def index(request):
    return render(request, 'tent/index.html')


def offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['first_name'])
    else:
        form = OfferForm()
    return render(request, 'tent/offer.html', {'form': form})
