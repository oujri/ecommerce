# Generated by Django 2.0.4 on 2018-05-31 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20180528_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]
