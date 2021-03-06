# Generated by Django 2.2.5 on 2019-11-25 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kardex', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kardex',
            name='fechaFin',
        ),
        migrations.RemoveField(
            model_name='kardex',
            name='fechaInicio',
        ),
        migrations.AddField(
            model_name='kardex',
            name='stockMaximo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kardex',
            name='stockMinimo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('idPeriodo', models.AutoField(primary_key=True, serialize=False)),
                ('fechaInicio', models.DateField()),
                ('fechaFinal', models.DateField(blank=True, null=True)),
                ('existenciaFinal', models.IntegerField()),
                ('saldoFinal', models.FloatField()),
                ('kardex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kardex.Kardex')),
            ],
        ),
        migrations.CreateModel(
            name='LineaPeriodo',
            fields=[
                ('idLineaPeriodo', models.AutoField(primary_key=True, serialize=False)),
                ('factura', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('tipoTransaccion', models.CharField(max_length=3)),
                ('valorUnitario', models.FloatField()),
                ('cantidadEntrada', models.IntegerField()),
                ('valorEntrada', models.FloatField()),
                ('cantidadSalida', models.IntegerField()),
                ('valorSalida', models.FloatField()),
                ('cantidadExistencia', models.IntegerField()),
                ('valorExistencia', models.FloatField()),
                ('comprobacion', models.FloatField()),
                ('cantidadSobrante', models.IntegerField()),
                ('compraAsociada', models.IntegerField()),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kardex.Periodo')),
            ],
        ),
    ]
