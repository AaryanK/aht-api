# Generated by Django 3.2.7 on 2022-04-06 18:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0009_alter_customerid_cid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='type',
            field=models.CharField(choices=[('ADULT', 'Adult'), ('CHILD', 'Child')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_class',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
