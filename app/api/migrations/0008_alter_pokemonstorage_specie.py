# Generated by Django 4.1.3 on 2022-12-02 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_pokemonstorage_is_party_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonstorage',
            name='specie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.pokemon'),
        ),
    ]