# Generated by Django 4.0.3 on 2022-03-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.CharField(choices=[('AIDS', 'aids'), ('CSE', 'cse'), ('CSIT', 'csit')], max_length=100),
        ),
    ]
