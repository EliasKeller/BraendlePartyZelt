from django.db import models
from django_enumfield import enum


class TentType(enum.Enum):
    FESTZELT = 0
    LEICHTBAUZELT = 1
    PAGODENZELT = 2

    labels = {
        FESTZELT: 'Festzelt',
        LEICHTBAUZELT: 'Leichtbauzelt',
        PAGODENZELT: 'Pagodenzelt'
    }


class Tent(models.Model):
    type = enum.EnumField(TentType, default=TentType.FESTZELT)
    width = models.IntegerField()
    length = models.IntegerField()
    number_of_People = models.IntegerField()
    price = models.IntegerField()
    tent_image = models.FileField(null=True)

    def __str__(self):
        return self.get_type_display()
