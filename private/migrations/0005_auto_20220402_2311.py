# Generated by Django 3.2.7 on 2022-04-02 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0004_auto_20220402_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='number_of_transactions',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='outstanding_payment',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='outstanding_payment_currency',
        ),
    ]
