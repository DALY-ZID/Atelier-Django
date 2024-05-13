from django.db import models
from datetime import date

# Create your models here.
class Categorie(models.Model):
    TYPE_CHOICES = [
        ('Lg', 'Linge de Maison'),
        ('Bj', 'Bijoux'),
        ('Dc', 'Décor'),
        ('Al','Alimentaire'),
        ('Mb','Meuble'),
        ('Sn','Sanitaire'),
        ('Vt','Vêtement'),
        ('Vs','Vaisselle'),
        ('Jx','Jouets')
    ]
    name = models.CharField(max_length = 50, default = 'Alimentaire', choices = TYPE_CHOICES)
    
    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    nom = models.CharField(max_length = 100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length = 8)

    def __str__(self):
        return self.nom + " " + self.adresse + " " + self.email + " " + self.telephone

class Produit(models.Model):
    TYPE_CHOICES = [('em','emballé'), ('fr','Frais'),('cs','Conserve')]
    libelle = models.CharField(max_length = 100)
    description = models.TextField()
    prix = models.DecimalField(max_digits = 10, decimal_places = 3)
    type = models.CharField(max_length = 2, choices = TYPE_CHOICES, default = 'em')
    Img = models.ImageField(blank = True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.libelle + " " + self.description + " " + str(self.prix) + " " + self.type

class ProduitNC(Produit):
    duree_garantie = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.__str__() + ' ' + self.duree_garantie

class Commande(models.Model):
    dateCde = models.DateField(null = True, default = date.today)
    totalCde = models.DecimalField(max_digits = 10, decimal_places = 3, default=0)
    produits = models.ManyToManyField('Produit')

    def allProducts(self):
        ch = " "
        for produit in self.produits.all():
            ch += "" + produit.__str__() +  ". "
        return ch
    
    def priceProducts(self):
        p = 0
        for produit in self.produits.all():
            p += produit.prix
        self.totalCde = p
        self.save()

    def __str__(self):
        return str(self.dateCde) + ' ' + str(self.totalCde) + ' ' + (self.allProducts())
