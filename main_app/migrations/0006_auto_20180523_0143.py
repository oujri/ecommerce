# Generated by Django 2.0.4 on 2018-05-23 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_profil_type_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='type_customer',
            field=models.CharField(choices=[('Ordinary', 'Ordinary'), ('Professional', 'Professional'), ('Supplier', 'Supplier'), ('Seller', 'Seller')], default='Ordinary', max_length=20),
        ),
    ]
