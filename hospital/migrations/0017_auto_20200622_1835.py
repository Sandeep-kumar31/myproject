# Generated by Django 3.0.5 on 2020-06-22 18:35
# flake8: noqa
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=consider-using-in
# pylint: disable=too-many-branches
# pylint: disable=inconsistent-return-statements
# pylint: disable=unused-argument
# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name
# pylint: disable=arguments-differ
# pylint: disable=no-else-return
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline
# pylint: disable=missing-final-newline
# pylint: disable=bare-except
# pylint: disable=unused-import
# pylint: disable=missing-function-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=consider-using-in
# pylint: disable=too-many-branches
# pylint: disable=inconsistent-return-statements
# pylint: disable=unused-argument
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-locals
# pylint: disable=singleton-comparison
# pylint: disable=wrong-import-order
# pylint: disable=duplicate-code
# pylint: disable=no-member
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0016_auto_20200622_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patientId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Doctor'),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='patientId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Patient'),
        ),
    ]
