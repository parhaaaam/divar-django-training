# Generated by Django 4.1 on 2022-08-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='unit_number',
            new_name='course_number',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='unit_name',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='finish_time',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='university_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='first_session',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='second_session',
        ),
        migrations.AddField(
            model_name='unit',
            name='first_day',
            field=models.CharField(default='0', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='second_day',
            field=models.CharField(default='0', max_length=10),
            preserve_default=False,
        ),
    ]
