from tent.models import Tent
import django_filters


class TentFilter(django_filters.FilterSet):
    class Meta:
        model = Tent
        fields = ['width', 'length', ]
