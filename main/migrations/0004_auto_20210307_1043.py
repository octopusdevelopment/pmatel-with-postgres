# Generated by Django 3.0.7 on 2021-03-07 09:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201121_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom du Produit')),
                ('slug', models.SlugField(max_length=70, unique=True, verbose_name='Slug')),
                ('sub_title', models.CharField(blank=True, max_length=100, verbose_name='Sous titre')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texte en Plus')),
                ('sup_info', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Informations Supplémentaires')),
                ('photo', models.ImageField(blank=True, upload_to=main.models.PathAndRename('produits/%Y/%m/%d/'), verbose_name='Photo du Produit')),
                ('photo_2', models.ImageField(blank=True, upload_to=main.models.PathAndRename('produits/%Y/%m/%d/'), verbose_name='Photo du Produit 2')),
                ('file_1', models.FileField(blank=True, upload_to='fichiers/', verbose_name='Fichier 1')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prix')),
                ('available', models.BooleanField(default=True, verbose_name='Disponibilité')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category', verbose_name='Catégorie')),
                ('solution', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Solution', verbose_name='Solution')),
            ],
        ),
        migrations.DeleteModel(
            name='Produit',
        ),
    ]
