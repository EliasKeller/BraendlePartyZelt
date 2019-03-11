from django.db import models
from django_enumfield import enum

class TentType(enum.Enum):
    FESTZELTE = 0
    LEICHTBAUZELTE = 1
    PAGODENZELTE = 2


class Tent(models.Model):
    type = enum.EnumField(TentType, default=TentType.FESTZELTE)
    width = models.IntegerField()
    length = models.IntegerField()
    number_of_People = models.IntegerField()
    price = models.IntegerField()

