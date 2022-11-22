# Generated by Django 4.1.2 on 2022-11-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('location', models.CharField(max_length=30)),
                ('budget', models.IntegerField()),
                ('company', models.CharField(max_length=30)),
            ],
        ),
    ]