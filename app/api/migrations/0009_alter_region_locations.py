# Generated by Django 4.1.3 on 2022-12-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_pokemonstorage_specie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='locations',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
