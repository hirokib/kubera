# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10, default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('trans_date', models.DateTimeField(verbose_name='Purchase Time')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, default=0.0)),
                ('customer', models.ForeignKey(to='mobile.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='balance',
            name='customer',
            field=models.ForeignKey(to='mobile.Customer'),
        ),
    ]
