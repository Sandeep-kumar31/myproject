# Generated by Django 3.0.5 on 2020-05-20 04:53
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


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctorName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patientName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(max_length=100),
        ),
    ]
