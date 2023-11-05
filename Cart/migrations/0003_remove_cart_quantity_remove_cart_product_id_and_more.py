# Generated by Django 4.2.6 on 2023-11-04 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_remove_product_brand_name_remove_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cart', '0002_alter_cart_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.AlterField(
            model_name='cart',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.ManyToManyField(to='Accounts.product'),
        ),
    ]
