# Generated by Django 4.0.3 on 2022-03-28 00:46

import DomiCercaBackend.defs
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domicilio', '0002_alter_domicilio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domicilio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=DomiCercaBackend.defs.media_upload_to, verbose_name='imagen'),
        ),
    ]
