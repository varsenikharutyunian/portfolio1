# Generated by Django 3.2.18 on 2023-07-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.TextField()),
                ('start_data', models.IntegerField()),
                ('end_data', models.IntegerField()),
                ('grade', models.TextField()),
            ],
        ),
    ]