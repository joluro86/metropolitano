# Generated by Django 3.2.7 on 2022-11-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionvencimientos', '0023_delete_faltanteperseo_delete_matfenix_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subzona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Subzona')),
            ],
            options={
                'verbose_name': 'Subzona',
                'verbose_name_plural': 'Subzona',
            },
        ),
    ]