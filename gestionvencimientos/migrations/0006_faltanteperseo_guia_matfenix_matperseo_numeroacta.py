# Generated by Django 4.0.6 on 2022-08-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionvencimientos', '0005_novedad_acta_item_novedad_acta_pagina_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='faltanteperseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concatenacion', models.CharField(default='0', max_length=100, verbose_name='Concat')),
                ('pedido', models.CharField(max_length=10, verbose_name='Pedido')),
                ('actividad', models.CharField(max_length=500, verbose_name='Actividad')),
                ('fecha', models.CharField(max_length=100, verbose_name='Fecha')),
                ('codigo', models.CharField(max_length=100, verbose_name='Código')),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Cantidad')),
                ('acta', models.CharField(default=0, max_length=100, verbose_name='Acta')),
                ('observacion', models.CharField(default='-', max_length=200, verbose_name='Observación')),
                ('cantidad_fenix', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Can Fenix')),
                ('diferencia', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Diferencia')),
            ],
            options={
                'verbose_name': 'Faltante Perseo',
                'verbose_name_plural': 'Faltante Perseo',
                'db_table': 'faltanteperseo',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_perseo', models.CharField(max_length=100, verbose_name='Nombre Perseo')),
                ('nombre_fenix', models.CharField(max_length=100, verbose_name='Nombre Fenix')),
            ],
            options={
                'verbose_name': 'guia',
                'verbose_name_plural': 'guias',
            },
        ),
        migrations.CreateModel(
            name='matfenix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concatenacion', models.CharField(default='0', max_length=100, verbose_name='Concat')),
                ('pedido', models.CharField(max_length=10, verbose_name='Pedido')),
                ('actividad', models.CharField(max_length=500, verbose_name='Actividad')),
                ('fecha', models.CharField(max_length=100, verbose_name='Fecha')),
                ('codigo', models.CharField(max_length=100, verbose_name='Código')),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Cantidad')),
                ('enperseo', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Material Fenix',
                'verbose_name_plural': 'Material Fenix',
                'db_table': 'fenix',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='matperseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concatenacion', models.CharField(default='0', max_length=100, verbose_name='Concat')),
                ('pedido', models.CharField(max_length=10, verbose_name='Pedido')),
                ('actividad', models.CharField(max_length=500, verbose_name='Actividad')),
                ('fecha', models.CharField(max_length=100, verbose_name='Fecha')),
                ('codigo', models.CharField(max_length=100, verbose_name='Código')),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Cantidad')),
                ('acta', models.CharField(default=0, max_length=100, verbose_name='Acta')),
                ('enfenix', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Material Perseo',
                'verbose_name_plural': 'Material Perseo',
                'db_table': 'perseo',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='NumeroActa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Acta actual',
                'verbose_name_plural': 'Acta actual',
            },
        ),
    ]
