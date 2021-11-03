# Generated by Django 3.2.7 on 2021-10-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_dicription_product_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='products.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
