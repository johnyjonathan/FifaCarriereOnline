# Generated by Django 4.0.4 on 2022-10-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIFACarrierApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playersdata',
            name='club_joined',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='playersdata',
            name='dob',
            field=models.CharField(max_length=30),
        ),
    ]