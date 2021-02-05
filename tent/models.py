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

    def __str__(self):
        return self.get_type_display()


class Tent(models.Model):
    type = enum.EnumField(TentType, default=TentType.FESTZELT)
    width = models.IntegerField()
    length = models.IntegerField()
    number_of_People = models.IntegerField()
    price = models.IntegerField()
    tent_image = models.FileField(null=True)

    def __str__(self):
        return self.width.__str__() + ' x ' + self.length.__str__()


class EquipmentType(enum.Enum):
    BANQUET_SET = 0
    BAR = 1
    FLOOR = 2
    HEATER = 3
    BOUNCY_CASTLE = 4
    VARIOUS = 5

    labels = {
        BANQUET_SET: 'Festbankgarnitur',
        BAR: 'Bar',
        FLOOR: 'Boden',
        HEATER: 'Heizung',
        BOUNCY_CASTLE: 'Hüpfburg',
        VARIOUS: 'Diverses'
    }


class Equipment(models.Model):
    type = enum.EnumField(EquipmentType, default=EquipmentType.BANQUET_SET)
    designation = models.CharField(max_length=250)
    size_Or_Power = models.CharField(max_length=250)
    price_fetched = models.IntegerField()
    price_delivered = models.IntegerField()
    equipment_image = models.FileField(null=True)

    def __str__(self):
        return self.designation + ' - ' + self.size_Or_Power
