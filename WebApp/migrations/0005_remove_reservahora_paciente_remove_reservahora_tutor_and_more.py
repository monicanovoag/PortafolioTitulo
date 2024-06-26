# Generated by Django 5.0.3 on 2024-04-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_alter_paciente_rut_alter_tutor_rut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservahora',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='reservahora',
            name='tutor',
        ),
        migrations.AddField(
            model_name='reservahora',
            name='apellidoPaciente',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservahora',
            name='emailPaciente',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservahora',
            name='nombrePaciente',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservahora',
            name='rutPaciente',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservahora',
            name='telefonoPaciente',
            field=models.CharField(default=1, max_length=9),
            preserve_default=False,
        ),
    ]
