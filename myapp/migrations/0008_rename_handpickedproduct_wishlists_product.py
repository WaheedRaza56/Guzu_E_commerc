# Generated by Django 4.2.3 on 2023-10-15 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_box_handpickedproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlists',
            old_name='handPickedProduct',
            new_name='product',
        ),
    ]
