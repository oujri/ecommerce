# Generated by Django 2.0.4 on 2018-05-31 23:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0058_auto_20180531_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor.fields.RichTextField(default=' '),
        ),
    ]
