# Generated by Django 3.2.18 on 2023-07-13 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_auto_20230713_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
