# Generated by Django 3.0.5 on 2021-09-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coviddata',
            name='last_updated',
            field=models.CharField(default='Last updated N/A', max_length=20),
            preserve_default=False,
        ),
    ]
