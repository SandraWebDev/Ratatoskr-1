# Generated by Django 4.2.1 on 2023-06-08 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_alter_timeslot_end_alter_timeslot_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='timeslot',
            name='Schedule_id',
        ),
        migrations.AddField(
            model_name='timeslot',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.schedule'),
        ),
    ]
