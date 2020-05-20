from django.contrib import admin

# Register your models here.
from .models import newsGiornalistiModel, newsArticoliModel
# Register your models here.

admin.site.register(newsGiornalistiModel)
admin.site.register(newsArticoliModel)