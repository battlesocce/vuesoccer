# Generated by Django 2.1.7 on 2020-08-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teamname',
            field=models.CharField(blank=True, default='Team_nameusers.CustomUser', max_length=100, null=True),
        ),
    ]
