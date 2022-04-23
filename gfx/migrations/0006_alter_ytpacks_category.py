# Generated by Django 4.0.3 on 2022-04-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfx', '0005_alter_ytpacks_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ytpacks',
            name='category',
            field=models.CharField(choices=[('NEO', 'Nawab Editz Outro'), ('AGG', 'Arpit Graphiz GFX Materials'), ('ABT', 'Aquas Brain Thumbnail'), ('NEG', 'Nawab Editz GFX Materials'), ('SSG', 'SS Graphics GFX Materials'), ('--', '------'), ('SST', 'SS Graphics Thumbnail'), ('NER', 'Nawab Editz Render'), ('AGP', 'Arpit Graphiz Poster'), ('ABO', 'Aquas Brain Outro'), ('ABI', 'Aquas Brain Intro'), ('ABB', 'Aquas Brain Banner'), ('AGB', 'Arpit Graphiz Banner'), ('AGT', 'Arpit Graphiz Thumbnail'), ('SSO', 'SS Graphics Outro'), ('SSI', 'SS Graphics Intro'), ('ABG', 'Aquas Brain GFX Materials'), ('AGR', 'Arpit Graphiz Render'), ('AGI', 'Arpit Graphiz Intro'), ('AGO', 'Arpit Graphiz Outro'), ('NET', 'Nawab Editz Thumbnail'), ('SSP', 'SS Graphics Poster'), ('SSR', 'SS Graphics Render'), ('NEI', 'Nawab Editz Intro'), ('NEP', 'Nawab Editz Poster'), ('ABP', 'Aquas Brain Poster'), ('NEB', 'Nawab Editz Banner'), ('ABR', 'Aquas Brain Render'), ('SSB', 'SS Graphics Banner')], default='--', max_length=90),
        ),
    ]
