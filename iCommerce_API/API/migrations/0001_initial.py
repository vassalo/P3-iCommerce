# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('totalPrice', models.FloatField()),
                ('date', models.DateField()),
                ('ostentacaoCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('isAdmin', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.User'),
        ),
    ]
