from django.shortcuts import render,HttpResponse
import datetime
def index(request): 
    return render(request, "home.html")