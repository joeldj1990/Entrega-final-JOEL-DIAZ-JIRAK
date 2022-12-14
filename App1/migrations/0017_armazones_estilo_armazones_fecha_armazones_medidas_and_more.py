# Generated by Django 4.1.3 on 2022-11-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0016_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='armazones',
            name='estilo',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='armazones',
            name='fecha',
            field=models.DateField(default='1111-11-11'),
        ),
        migrations.AddField(
            model_name='armazones',
            name='medidas',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='armazones',
            name='peso',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='armazones',
            name='tipo',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='cristales',
            name='duracion',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='cristales',
            name='fecha',
            field=models.DateField(default='1111-11-11'),
        ),
        migrations.AddField(
            model_name='cristales',
            name='laboratorio',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='cristales',
            name='prescripcion',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AddField(
            model_name='lentes_sol',
            name='antireflejo',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='lentes_sol',
            name='estilo',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='lentes_sol',
            name='fecha',
            field=models.DateField(default='1111-11-11'),
        ),
        migrations.AddField(
            model_name='lentes_sol',
            name='medidas',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='lentes_sol',
            name='peso',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='lentes_sol',
            name='polarizado',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='lentes_sol',
            name='tipo',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='cristales',
            name='graduacion',
            field=models.CharField(max_length=30),
        ),
    ]
