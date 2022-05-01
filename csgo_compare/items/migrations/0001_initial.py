# Generated by Django 4.0.3 on 2022-05-01 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=400)),
                ('icon_large', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('icon', models.CharField(blank=True, max_length=400, null=True)),
                ('icon_large', models.CharField(blank=True, max_length=400, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('icon', models.CharField(max_length=400)),
                ('icon_large', models.CharField(max_length=400)),
                ('lowest_float', models.FloatField(blank=True, null=True)),
                ('highest_float', models.FloatField(blank=True, null=True)),
                ('stattrak', models.BooleanField(default=False)),
                ('souvenir', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.collection')),
                ('rarity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.rarity')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=400)),
                ('icon_large', models.CharField(max_length=400)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.collection')),
            ],
        ),
    ]
