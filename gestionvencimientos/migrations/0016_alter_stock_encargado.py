# Generated by Django 4.0.6 on 2022-08-29 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionvencimientos', '0015_stock_diferencia_alter_stock_despachado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='encargado',
            field=models.CharField(default='0', max_length=300, verbose_name='Oficial'),
        ),
    ]
