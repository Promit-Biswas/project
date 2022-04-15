# Generated by Django 4.0.3 on 2022-04-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0010_appointment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Receptionist',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phonenumber',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='patient',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phonenumber',
            field=models.CharField(max_length=11),
        ),
    ]
