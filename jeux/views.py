from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Bonjour Ceci Mon Première Jeux Django")
