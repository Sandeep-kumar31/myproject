# Generated by Django 3.0.5 on 2020-05-15 04:45
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
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.PositiveIntegerField()),
                ('joindate', models.DateField(auto_now_add=True)),
                ('mobile', models.CharField(max_length=40)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=40, null=True)),
                ('symptoms', models.CharField(max_length=100, null=True)),
                ('assignedDoctorId', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=40, null=True)),
                ('department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
