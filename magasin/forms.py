from django.forms import ModelForm
from .models import Produit, Fournisseur, Commande
class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"  # pour tous les champs de la table

    def __init__(self, *args, **kwargs):
        super(ProduitForm, self).__init__(*args, **kwargs)
        self.fields['Img'].widget.attrs['accept'] = 'image/*'
    
class FournisseurForm(ModelForm):
    class Meta :
        model = Fournisseur
        fields = "__all__" #pour tous les champs de la table
        # fields=['nom','adresse'] #pour qulques champs

class CommandeForm(ModelForm):
    class Meta :
        model = Commande
        fields = ['dateCde', 'produits'] #pour tous les champs de la table
        # fields=['nom','adresse'] #pour qulques champs

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')