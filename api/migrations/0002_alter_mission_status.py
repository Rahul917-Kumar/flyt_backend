# Generated by Django 5.2.3 on 2025-06-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='status',
            field=models.CharField(choices=[('planned', 'Planned'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('aborted', 'Aborted'), ('paused', 'Paused')], default='planned', max_length=20),
        ),
    ]
