# Generated by Django 4.2.1 on 2023-06-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_alter_timeslot_schedule_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
