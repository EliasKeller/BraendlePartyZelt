from django.shortcuts import render
from django.views import generic
from tent.forms import OfferForm
from .models import Tent


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


class PartyTentView(generic.ListView):
    template_name = 'tent/partyTent.html'
    context_object_name = 'all_tents'

    def get_queryset(self):
        return Tent.objects.all()
