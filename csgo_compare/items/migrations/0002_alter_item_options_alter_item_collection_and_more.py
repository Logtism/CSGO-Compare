# Generated by Django 4.0.4 on 2022-05-09 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'permissions': (('can_view_item_sub', 'Can view new item submissions'), ('can_accept_item_sub', 'Can accept item submissions.'), ('can_decline_item_sub', 'Can decline item submissions'))},
        ),
        migrations.AlterField(
            model_name='item',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection_items', to='items.collection'),
        ),
        migrations.AlterField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='items.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='items.category'),
        ),
    ]
