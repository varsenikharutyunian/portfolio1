# Generated by Django 3.2.18 on 2023-07-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_delete_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_possition', models.TextField()),
                ('start_data', models.DateField()),
                ('end_data', models.DateField()),
                ('is_current', models.BooleanField()),
                ('addres', models.TextField()),
                ('job_description', models.TextField()),
                ('company_name', models.TextField()),
            ],
        ),
    ]
