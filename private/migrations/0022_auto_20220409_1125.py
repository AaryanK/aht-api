# Generated by Django 3.2.7 on 2022-04-09 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0021_auto_20220407_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingticket',
            name='booking',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='private.booking'),
        ),
        migrations.RemoveField(
            model_name='bookingticket',
            name='ticket',
        ),
        migrations.AddField(
            model_name='bookingticket',
            name='ticket',
            field=models.ManyToManyField(to='private.Ticket'),
        ),
    ]
