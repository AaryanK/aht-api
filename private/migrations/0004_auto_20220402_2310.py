# Generated by Django 3.2.7 on 2022-04-02 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0003_auto_20220402_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='bills',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='ticket',
        ),
        migrations.AddField(
            model_name='bill',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='private.customer'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='passenger_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='private.customer'),
        ),
    ]
