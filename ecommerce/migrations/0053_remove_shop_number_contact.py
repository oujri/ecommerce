# Generated by Django 2.0.4 on 2018-05-28 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0052_auto_20180528_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='number_contact',
        ),
    ]