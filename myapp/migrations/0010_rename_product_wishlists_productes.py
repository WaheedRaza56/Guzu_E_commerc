# Generated by Django 4.2.3 on 2023-10-26 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_wishlists_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlists',
            old_name='product',
            new_name='productes',
        ),
    ]
