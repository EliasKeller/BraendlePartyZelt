from django.db import models


class Offer(models.Model):
    managed = False
    customer_name = models.CharField(max_length=250)
    offer_description = models.CharField(max_length=500)
