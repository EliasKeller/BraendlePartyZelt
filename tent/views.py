from django.shortcuts import render
from tent.forms import OfferForm
from .models import Tent, TentType
from .filters import PartyTentFilter


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


#class PartyTentView(generic.ListView):
#    template_name = 'tent/partyTent.html'
#    context_object_name = 'all_tents'

#    def get_queryset(self):
#        return Tent.objects.filter(type=TentType.FESTZELT)

def partyTentView(request):
    partyTent_list = Tent.objects.all()
    partyTent_filter = PartyTentFilter(request.GET, queryset=partyTent_list)
    return render(request, 'tent/partyTent.html', {'filter': partyTent_filter})
