# Generated by Django 4.1.3 on 2022-12-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_location_region_locations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abilities', models.JSONField(null=True)),
                ('capture_rate', models.FloatField(default=0)),
                ('color', models.CharField(default='', max_length=100)),
                ('flavor_text', models.CharField(default='', max_length=400)),
                ('height', models.FloatField(default=0)),
                ('moves', models.JSONField(null=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('sprites', models.JSONField(null=True)),
                ('stats', models.JSONField(null=True)),
                ('types', models.JSONField(null=True)),
                ('weight', models.JSONField(null=True)),
            ],
        ),
    ]