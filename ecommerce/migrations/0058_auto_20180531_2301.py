# Generated by Django 2.0.4 on 2018-05-31 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0057_auto_20180531_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
