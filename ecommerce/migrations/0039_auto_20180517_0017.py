# Generated by Django 2.0.4 on 2018-05-17 00:17

from django.db import migrations, models
import django.db.models.deletion
import ecommerce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0038_auto_20180516_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='user',
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, upload_to=ecommerce.models.PathAndRename('images/2018/05/17')),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='commercecategory',
            name='image',
            field=models.ImageField(default='/images/categories.jpg', upload_to=ecommerce.models.PathAndRename('images/2018/05/17')),
        ),
        migrations.AlterField(
            model_name='commerceimage',
            name='image',
            field=models.ImageField(upload_to=ecommerce.models.PathAndRename('images/2018/05/17')),
        ),
        migrations.AlterField(
            model_name='compare',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Shipped', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/images/categories.jpg', upload_to=ecommerce.models.PathAndRename('images/2018/05/17')),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to=ecommerce.models.PathAndRename('slides/2018/05/17')),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil'),
        ),
        migrations.DeleteModel(
            name='Profil',
        ),
    ]
