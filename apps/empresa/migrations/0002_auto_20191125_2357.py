# Generated by Django 2.2.5 on 2019-11-25 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nrc',
            field=models.CharField(max_length=10),
        ),
    ]
