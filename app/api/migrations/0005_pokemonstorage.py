# Generated by Django 4.1.3 on 2022-12-01 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_pokemon'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(default='pokemon', max_length=100)),
                ('is_party_member', models.BooleanField(default=False)),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.pokemon')),
            ],
        ),
    ]
