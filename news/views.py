from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .models import newsArticoliModel, newsGiornalistiModel


def home(request): 
    return render(request, "home.html")

class listaArticoliView(ListView):
    model = newsArticoliModel #modello dei dati da utilizzare 
    template_name = "news/articoli.html"  #pagina per mostrare i dati

class listaGiornalistiView(ListView):
    model = newsGiornalistiModel #modello dei dati da utilizzare 
    template_name = "news/giornalisti.html"  #pagina per mostrare i dati
# Create your views here.

