# Generated by Django 5.0.2 on 2024-02-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0002_categorie_fournisseur_produitnc_produit_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor'), ('Al', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vt', 'Vêtement'), ('Vs', 'Vaisselle'), ('Jx', 'Jouets')], default='Alimentaire', max_length=50),
        ),
    ]
