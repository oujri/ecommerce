# Generated by Django 2.0.4 on 2018-05-04 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commercecategory',
            old_name='nom',
            new_name='name',
        ),
    ]
