# Generated by Django 4.0.3 on 2022-04-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfx', '0006_product_is_deleted_ytpacks_is_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='trending',
        ),
        migrations.AlterField(
            model_name='ytpacks',
            name='category',
            field=models.CharField(choices=[('ABT', 'Aquas Brain Thumbnail'), ('AGT', 'Arpit Graphiz Thumbnail'), ('NEB', 'Nawab Editz Banner'), ('ABG', 'Aquas Brain GFX Materials'), ('NEP', 'Nawab Editz Poster'), ('AGB', 'Arpit Graphiz Banner'), ('SSG', 'SS Graphics GFX Materials'), ('SSI', 'SS Graphics Intro'), ('ABP', 'Aquas Brain Poster'), ('NEG', 'Nawab Editz GFX Materials'), ('--', '------'), ('NEI', 'Nawab Editz Intro'), ('ABO', 'Aquas Brain Outro'), ('SSB', 'SS Graphics Banner'), ('AGR', 'Arpit Graphiz Render'), ('AGP', 'Arpit Graphiz Poster'), ('AGO', 'Arpit Graphiz Outro'), ('NEO', 'Nawab Editz Outro'), ('AGG', 'Arpit Graphiz GFX Materials'), ('AGI', 'Arpit Graphiz Intro'), ('ABB', 'Aquas Brain Banner'), ('NET', 'Nawab Editz Thumbnail'), ('SSR', 'SS Graphics Render'), ('ABI', 'Aquas Brain Intro'), ('SSP', 'SS Graphics Poster'), ('NER', 'Nawab Editz Render'), ('ABR', 'Aquas Brain Render'), ('SST', 'SS Graphics Thumbnail'), ('SSO', 'SS Graphics Outro')], default='--', max_length=90),
        ),
    ]
