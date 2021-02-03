from django.shortcuts import render
from tent.forms import OfferForm
from .models import Tent, TentType, Equipment
from .filters import TentFilter


def index(request):
    return render(request, 'tent/index.html')


def party_tent_search(request):
    party_tent_list = Tent.objects.filter(type=TentType.FESTZELT)
    party_tent_filter = TentFilter(request.GET, queryset=party_tent_list)
    return render(request, 'tent/partyTent.html', {'filter': party_tent_filter})


def equipment(request):
    equipment_list = Equipment.objects.all()
    return render(request, 'tent/equipment.html', {'equipment_list': equipment_list})


def offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['first_name'])
    else:
        form = OfferForm()
    return render(request, 'tent/offer.html', {'form': form})


def aboutMe(request):
    return render(request, 'tent/aboutMe.html')
