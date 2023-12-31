# Generated by Django 3.2.18 on 2023-07-12 07:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_experience_compani_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='start_data',
        ),
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1900)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1900)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='grade',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='university_name',
            field=models.TextField(max_length=70),
        ),
        migrations.AlterField(
            model_name='experience',
            name='addres',
            field=models.TextField(max_length=70),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.TextField(max_length=70),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_data',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_data',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='skill',
            name='value',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
