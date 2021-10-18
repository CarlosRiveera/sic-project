# Generated by Django 2.2.5 on 2019-11-17 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kardex', '0001_initial'),
        ('transaccionInventario', '0002_transaccioninventario_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActualizacionInventario',
            fields=[
                ('idActualzacion', models.AutoField(primary_key=True, serialize=False)),
                ('existencias', models.IntegerField()),
                ('costoUnitario', models.FloatField()),
                ('costoTotal', models.FloatField()),
                ('kardex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kardex.Kardex')),
                ('transaccionInventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaccionInventario.TransaccionInventario')),
            ],
        ),
    ]