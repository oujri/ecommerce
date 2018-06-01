# Generated by Django 2.0.4 on 2018-05-31 01:29

from django.db import migrations, models
import ecommerce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0056_auto_20180530_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_payment',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, upload_to=ecommerce.models.PathAndRename('images/2018/05/31')),
        ),
        migrations.AlterField(
            model_name='commercecategory',
            name='image',
            field=models.ImageField(default='/images/categories.jpg', upload_to=ecommerce.models.PathAndRename('images/2018/05/31')),
        ),
        migrations.AlterField(
            model_name='commerceimage',
            name='image',
            field=models.ImageField(upload_to=ecommerce.models.PathAndRename('images/2018/05/31')),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Created', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/images/categories.jpg', upload_to=ecommerce.models.PathAndRename('images/2018/05/31')),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image_cover',
            field=models.ImageField(default='/images/categories.jpg', upload_to=ecommerce.models.PathAndRename('images/2018/05/31')),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image_profile',
            field=models.ImageField(default='/images/categories.jpg', upload_to=ecommerce.models.PathAndRename('images/2018/05/31')),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to=ecommerce.models.PathAndRename('slides/2018/05/31')),
        ),
    ]
