# Generated by Django 3.0.6 on 2020-05-14 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_deaths', models.CharField(max_length=20)),
                ('total_infections', models.CharField(max_length=20)),
            ],
        ),
    ]
