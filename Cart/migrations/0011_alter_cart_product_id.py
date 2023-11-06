# Generated by Django 4.2.7 on 2023-11-05 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_alter_product_image_alter_product_product_name'),
        ('Cart', '0010_alter_cart_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Accounts.product'),
        ),
    ]
