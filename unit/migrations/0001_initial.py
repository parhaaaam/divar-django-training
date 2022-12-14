# Generated by Django 4.1 on 2022-08-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=256)),
                ('unit_name', models.CharField(max_length=256)),
                ('group_number', models.IntegerField()),
                ('unit_number', models.IntegerField()),
                ('teacher', models.CharField(max_length=256)),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
                ('first_session', models.DateField()),
                ('second_session', models.DateField()),
            ],
        ),
    ]
