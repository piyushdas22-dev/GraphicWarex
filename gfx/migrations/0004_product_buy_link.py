# Generated by Django 4.0.3 on 2022-04-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfx', '0003_alter_product_category_alter_product_dp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='buy_link',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]
