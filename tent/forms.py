from django.forms import ModelForm
from tent.models import Offer


class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['customer_name', 'offer_description']
