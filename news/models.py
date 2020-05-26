from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class newsGiornalistiModel(models.Model):
    
    nome = models.CharField(max_length=100)
   
   # data_creazione = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        #return reverse("PostDetailView", kwargs={"pk": self.pk})
        return f"/blog/leggi-post/{self.id}"


class newsArticoliModel(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    autore = models.ForeignKey(newsGiornalistiModel, on_delete=models.CASCADE, related_name="articoli")
   # data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        #return reverse("PostDetailView", kwargs={"pk": self.pk})
        return f"/blog/leggi-articolo/{self.id}"
