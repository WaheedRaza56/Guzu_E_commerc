# Generated by Django 4.2.3 on 2023-10-12 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_product_box_handpicked_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='box',
            old_name='handPicked_product',
            new_name='handPickedProduct',
        ),
        migrations.RenameField(
            model_name='wishlists',
            old_name='handPicked_product',
            new_name='handPickedProduct',
        ),
    ]
