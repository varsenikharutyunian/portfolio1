# Generated by Django 3.2.18 on 2023-07-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='compani_logo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
