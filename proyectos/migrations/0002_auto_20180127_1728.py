# Generated by Django 2.0 on 2018-01-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyectoprivado',
            old_name='imagenes',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='proyectopublico',
            old_name='imagenes',
            new_name='img1',
        ),
        migrations.AddField(
            model_name='proyectoprivado',
            name='img10',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectoprivado',
            name='img2',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectoprivado',
            name='img3',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectoprivado',
            name='img4',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectoprivado',
            name='img5',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectoprivado',
            name='img6',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectoprivado',
            name='img7',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectoprivado',
            name='img8',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectoprivado',
            name='img9',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectopublico',
            name='img10',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectopublico',
            name='img2',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectopublico',
            name='img3',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectopublico',
            name='img4',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectopublico',
            name='img5',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectopublico',
            name='img6',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectopublico',
            name='img7',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectopublico',
            name='img8',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
        migrations.AddField(
            model_name='proyectopublico',
            name='img9',
            field=models.FileField(blank=True, null=True, upload_to='img_proyectos/'),
        ),
    ]
