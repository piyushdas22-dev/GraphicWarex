# Generated by Django 4.0.3 on 2022-04-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_trendingslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partners', models.IntegerField(blank=True)),
                ('packs', models.IntegerField(blank=True)),
                ('monthly', models.IntegerField(blank=True)),
                ('daily', models.IntegerField(blank=True)),
            ],
        ),
    ]
