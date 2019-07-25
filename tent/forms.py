from django import forms
from material import Layout, Row, Span3


class OfferForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=250, label="Vorname")
    last_name = forms.CharField(required=True, max_length=250, label="Nachname")
    street = forms.CharField(required=True, max_length=250, label="Strasse")
    plz = forms.IntegerField(required=True, label="PLZ")
    place = forms.CharField(required=True, max_length=250, label="Ort")
    phone = forms.IntegerField(required=False, label='Telefon')
    phone_mobile = forms.IntegerField(required=True, label='Mobil')
    email = forms.EmailField(required=True, label='E-Mail')
    fax = forms.IntegerField(required=False)
    date_of_event = forms.DateField(required=True, label='Datum des Anlasses')
    plz_of_event = forms.IntegerField(required=True, label="PLZ Montageort")
    place_of_event = forms.CharField(required=True, max_length=250, label="Montageort")
    date_of_installation = forms.DateField(required=False, label='Aufbau ab')
    date_of_destruction = forms.DateField(required=False, label='Abbau ab')
    comment = forms.CharField(required=False, max_length=500, label='Bemerkung')

    layout = Layout(
        Row('first_name', 'last_name'),
        'street',
        Row('plz', Span3('place')),
        Row('phone', 'phone_mobile'),
        Row('email', 'fax'),
        'date_of_event',
        Row('plz_of_event', Span3('place_of_event')),
        Row('date_of_installation', 'date_of_destruction'),
        'comment',
    )

