import django_filters
from .models import Tent


class PartyTentFilter(django_filters.FilterSet):

    class Meta:
        model = Tent
        fields = ('type', 'width', 'length')
