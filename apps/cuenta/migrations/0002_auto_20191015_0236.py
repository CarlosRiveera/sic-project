# Generated by Django 2.2.5 on 2019-10-15 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='codigoCuenta',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='cuentaPadre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuenta.Cuenta'),
        ),
    ]
