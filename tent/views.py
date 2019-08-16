from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from tent.forms import OfferForm
from .models import Tent, TentType, Equipment
from .filters import TentFilter
from django.contrib import messages


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
            subject = 'Offertenanfrage von ' + form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
            from_email = 'offertenanfrage.bpz@gmail.com'
            to_email = ['elias.keller@gmail.com']
            content = '<p>Vorname: ' + form.cleaned_data['first_name'] + '</p>' \
                      '<p>Nachname: ' + form.cleaned_data['last_name'] + '</p>' \
                      '<p>Strasse: ' + form.cleaned_data['street'] + '</p>' \
                      '<p>PLZ: ' + str(form.cleaned_data['plz']) + '</p>' \
                      '<p>Ort: ' + form.cleaned_data['place'] + '</p>' \
                      '<p>Tel-Nummer: ' + str(form.cleaned_data['phone']) + '</p>' \
                      '<p>Tel-Nummer (mobile): ' + str(form.cleaned_data['phone_mobile']) + '</p>' \
                      '<p>E-Mail: ' + form.cleaned_data['email'] + '</p>' \
                      '<p>Fax: ' + str(form.cleaned_data['fax']) + '</p>' \
                      '<p>Datum des Anlasses: ' + str(form.cleaned_data['date_of_event']) + '</p>' \
                      '<p>PLZ Montageort: ' + str(form.cleaned_data['plz_of_event']) + '</p>' \
                      '<p>Montageort: ' + form.cleaned_data['place_of_event'] + '</p>' \
                      '<p>Aufbau ab: ' + str(form.cleaned_data['date_of_installation']) + '</p>' \
                      '<p>Abbau ab: ' + str(form.cleaned_data['date_of_destruction']) + '</p>' \
                      '<p>Bemerkung: ' + form.cleaned_data['comment'] + '</p>'

            msg = EmailMultiAlternatives(subject, content, from_email, to_email)
            msg.attach_alternative(content, "text/html")
            msg.send()
            messages.success(request, "Brändle Partyzelt erfolgreich kontaktiert!")
    else:
        form = OfferForm()
    return render(request, 'tent/offer.html', {'form': form})
