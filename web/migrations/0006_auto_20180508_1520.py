# Generated by Django 2.0.5 on 2018-05-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20180507_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracioninicio',
            name='imgbanner1',
            field=models.CharField(choices=[('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto1'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto2'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto3')], max_length=1000, verbose_name='Imagen de Banner 1'),
        ),
        migrations.AlterField(
            model_name='configuracioninicio',
            name='imgbanner2',
            field=models.CharField(choices=[('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto1'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto2'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto3')], max_length=1000, verbose_name='Imagen de Banner 2'),
        ),
        migrations.AlterField(
            model_name='configuracioninicio',
            name='imgbanner3',
            field=models.CharField(choices=[('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto1'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto2'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto3')], max_length=1000, verbose_name='Imagen de Banner 3'),
        ),
        migrations.AlterField(
            model_name='configuracioninicio',
            name='proyectoventa1',
            field=models.CharField(choices=[('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto1'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto2'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto3')], max_length=1000, verbose_name='Proyecto en venta 1'),
        ),
        migrations.AlterField(
            model_name='configuracioninicio',
            name='proyectoventa2',
            field=models.CharField(choices=[('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto1'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto2'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto3')], max_length=1000, verbose_name='Proyecto en venta 2'),
        ),
        migrations.AlterField(
            model_name='configuracioninicio',
            name='proyectoventa3',
            field=models.CharField(choices=[('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto1'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto2'), ('0 ProyectoPrivado', 'ProyectoPrivado: Proyecto3')], max_length=1000, verbose_name='Proyecto en venta 3'),
        ),
    ]
