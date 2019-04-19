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


class EquipmentType(enum.Enum):
    INVENTORY = 0
    FLOOR = 1
    HEATER = 2
    BOUNCY_CASTLE = 3

    labels = {
        INVENTORY: 'Inventar',
        FLOOR: 'Boden',
        HEATER: 'Heizung',
        BOUNCY_CASTLE: 'Hüpfburg',
    }


class Equipment(models.Model):
    type = enum.EnumField(EquipmentType, default=EquipmentType.INVENTORY)
    designation = models.CharField(max_length=250)
    size_Or_Power = models.CharField(max_length=250)
    price_fetched = models.IntegerField()
    price_delivered = models.IntegerField()
    equipment_image = models.FileField(null=True)

    def __str__(self):
        return self.get_type_display()
