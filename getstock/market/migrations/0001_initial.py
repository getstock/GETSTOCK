# Generated by Django 3.1.2 on 2020-10-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=20)),
                ('buy_cost', models.CharField(max_length=10)),
                ('sell_cost', models.CharField(max_length=10)),
            ],
        ),
    ]
