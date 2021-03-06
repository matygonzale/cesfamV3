# Generated by Django 4.0.5 on 2022-06-24 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('prescripcion', '0001_initial'),
        ('medicamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='idCarnet_Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.carnet_paciente'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='idPrescripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescripcion.prescripcion'),
        ),
        migrations.AddField(
            model_name='reg_entregas',
            name='idCarnet_Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.carnet_paciente'),
        ),
        migrations.AddField(
            model_name='reg_entregas',
            name='idFarmaceuta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.farmaceuta'),
        ),
        migrations.AddField(
            model_name='reg_entregas',
            name='idMedicamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medicamento.medicamento'),
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='idCarnet_Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.carnet_paciente', verbose_name='Carnet Paciente '),
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='idDoctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.doctor'),
        ),
        migrations.AddField(
            model_name='cita_medica',
            name='idDoctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.doctor'),
        ),
        migrations.AddField(
            model_name='cita_medica',
            name='idPaciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.paciente'),
        ),
        migrations.AddField(
            model_name='cita_medica',
            name='idPrescripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prescripcion.prescripcion'),
        ),
    ]
