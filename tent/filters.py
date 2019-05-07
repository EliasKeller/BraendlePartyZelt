from tent.models import Tent
from django_filters import RangeFilter
import django_filters


class TentFilter(django_filters.FilterSet):
    width= django_filters.NumberFilter(label="Breite")
    length= django_filters.NumberFilter(label="Länge")
    number_of_People = RangeFilter(label="People range")

    class Meta:
        model = Tent
        fields = ['width', 'length', 'number_of_People', ]
