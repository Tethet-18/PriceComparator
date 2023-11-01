# Generated by Django 4.2.6 on 2023-11-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('brand_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('brand_logo', models.ImageField(upload_to='images/Brands')),
                ('brand_website', models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.URLField(max_length=3000)),
                ('product_name', models.CharField(max_length=255)),
                ('brand_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('image', models.ImageField(upload_to='images/Products')),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('reset_token', models.CharField(max_length=100)),
            ],
        ),
    ]