# Generated by Django 3.1.2 on 2020-10-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='stocks',
            field=models.ManyToManyField(to='market.Stock'),
        ),
    ]
