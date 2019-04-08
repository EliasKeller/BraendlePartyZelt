from tent.models import Tent
from django_filters import RangeFilter
import django_filters


class TentFilter(django_filters.FilterSet):
    number_of_People = RangeFilter(label="People range")

    class Meta:
        model = Tent
        fields = ['width', 'length', 'number_of_People', ]



