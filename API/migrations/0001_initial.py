# Generated by Django 4.0.6 on 2022-07-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('money', models.PositiveIntegerField()),
                ('population', models.PositiveIntegerField()),
                ('army', models.BooleanField(default=False)),
            ],
        ),
    ]
