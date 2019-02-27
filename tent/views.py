from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'tent/index.html')


def offer(request):
    return render(request, 'tent/offer.html')
