# Generated by Django 4.0.4 on 2022-10-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIFACarrierApp', '0003_alter_playersdata_club_joined_alter_playersdata_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersdata',
            name='club_flag_url',
            field=models.CharField(blank='True', max_length=200),
        ),
    ]
