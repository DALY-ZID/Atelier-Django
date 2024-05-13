from django.http import HttpResponseRedirect
from .models import Produit, Fournisseur, Commande
from .forms import ProduitForm, FournisseurForm, CommandeForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer, ProductSerializer

def index(request):
    products = Produit.objects.all()
    context = {'products':products}
    return render(request,'magasin/vitrine.html',context)

def ListPrd(request):
    products = Produit.objects.all()
    context = {'products':products}
    return render(request,'magasin/mesProduits.html',context)

def ListFrs(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs':fournisseurs}
    return render(request,'magasin/mesFournisseurs.html',context)

def ListCmd(request):
    commandes = Commande.objects.all()
    context = {'commandes': commandes, }
    return render(request, 'magasin/mesCommandes.html', context)

def AddProduct(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm() 
    return render(request,'magasin/majProduits.html',{'form':form})

def AddFrs(request):
    if request.method == "POST" :
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = FournisseurForm() 
    return render(request,'magasin/majFournisseurs.html',{'form':form})

def AddCmd(request):
    if request.method == "POST" :
        form = CommandeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = CommandeForm(initial={'totalCde': 0})
    return render(request,'magasin/majCommandes.html',{'form':form})

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            # return redirect('home')
            return HttpResponseRedirect('/magasin')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProductAPIView(APIView):
    def get(self, *args, **kwargs):
        products = Produit.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

from rest_framework import viewsets
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset