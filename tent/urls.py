from django.urls import path
from . import views

app_name = "tent"

urlpatterns = [
    path('', views.index, name='index'),
    path('offer/', views.offer, name='offer'),
    path('partyzelte/', views.party_tent_search, name='party_tent_search')
]
