# Generated by Django 3.0.2 on 2020-01-25 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='doctor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedule_doctor_name', to='main.Doctor'),
        ),
    ]