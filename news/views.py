from django.shortcuts import render
from django.views.generic.list import ListView
from .models import newsArticoliModel, newsGiornalistiModel
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, "home.html")

class listaArticoliView(ListView):
    model = newsArticoliModel
    template_name = 'news/articoli.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"] = newsArticoliModel.objects.all()
        return context

def listaArticoliGiornalistaView(request,pk):
    giornalista=get_object_or_404(newsGiornalistiModel, id=pk)
    articoli=giornalista.articoli.all()
    context = {'giornalista': giornalista,
               'articoli': articoli,
               }
    return render(request, 'news/articoli.html', context)

class listaGiornalistiView(ListView):
    model = newsGiornalistiModel
    template_name = 'news/giornalisti.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["giornalisti"] = newsGiornalistiModel.objects.all()
        return context