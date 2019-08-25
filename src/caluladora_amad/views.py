#Model View Template (MVT)
from django.http import HttpResponse
from django.shortcuts import render #Nos sirve paa visualiar la plantilla html




def home_page(request): # se define la pagina principal 
    
    return render(request, "login.html")